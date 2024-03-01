import csv
import itertools
import matplotlib.pyplot as plt
from matplotlib.ticker import LogFormatter


zip_longest = itertools.zip_longest
REDIS_LOGS_DIR = "logs/sinrabia/"
RABIA_LOGS_DIR = "logs/rabia/"
REDIS_LOGFILE = "redislog"
RABIA_LOGFILE = "rabialog"
LOG_EXTENSION = ".log"
SINSMR_COLOR = (1.0, 0.5, 0.0) # dark orange
SMR_RABIA_COLOR = 'blue'
'''
readLogFiles: read log files and generate a list of operations executed by each replica
input: list of log files
output: decisions of each replicas. Eg [decisionsR1, decisionsR2, decisionsR3]
'''
def readLogFiles(listLogFiles):
    # Open files
    listCsvReaders = []
    filesObjects = []
    for file in listLogFiles:
        f = open(file)
        filesObjects.append(f)
        csvReader = csv.reader(f, delimiter=" ")
        listCsvReaders.append(csvReader)

    # Start reading files
    filesRead = 0
    decisions = []
    sumSetsGets = []
    for logfile in listCsvReaders:
        decisionReplica = []
        prevState = 3.650000
        numLine = 0
        setCmds = 0
        getCmds = 0
        for lineList in logfile:
            # Logic
            # Ignore metadata 
            numLine += 1
            if len(lineList) <= 1: continue    # Blank line [] or ['OK']
            if lineList[3] == "hello" or lineList[3] == "ping": continue
            # If operation is GET (set prev state in decision array for this replica)
            if lineList[3] == "get":
                decisionReplica.append(prevState)
                getCmds += 1
            # elif operation is SET (set new state in decision array for this replica)
            elif lineList[3] == "set":
                prevState = lineList[5]     # update previous state with new state
                decisionReplica.append(prevState)
                setCmds += 1
            else:
                # shoudn't happen: panic and exit
                print("Error: Operation not recognized: Op# " + str(numLine) + lineList)
                exit(1)
        # Read file done
        decisions.append(decisionReplica)
        # insert setCmds and getCmds in sumSetsGets as tuplas
        sumSetsGets.append((setCmds, getCmds))
        # Close current file and go for next one
        filesObjects[filesRead].close()
        filesRead += 1
    # print summary results
    print("Total read files: " + str(filesRead))
    # return results
    return decisions, sumSetsGets

'''
printSummaryResults: print summary results of log analysis
'''
def printSummaryResults(decisions, summary):
    print("-- Summary Results --")
    for index, replica in enumerate(decisions):
        # print index of iteration
        print('Decisions Replica # {}'.format(index))
        print(replica)
    print("Sets and Gets Commands:")
    print(summary)
    return


'''
checkConsistency: verify consistency logs finding differences
output: #inconsistencies
'''
def checkConsistency(decisions):
    # SanityCheck: verify length of each replica's decisions
    lenArr = len(decisions[0])
    for i in range(len(decisions)):
        if len(decisions[i]) != lenArr:
            print("Panic Error: Replica " + str(i) + " has different length")
            exit(1)
    # compare each value of each array
    countDiff = 0
    for i in range(lenArr):
        curState = decisions[0][i]
        for j in range(1, len(decisions)):
            if curState != decisions[j][i]:
                countDiff += 1
                if lenArr <= 100:
                    # print inconsistency detail to console
                    print("Inconsistencia #" + str(countDiff) + ": Replicas have different value in #operation " + str(i))
                    for k in range(len(decisions)):
                        print("Replica #" + str(k) + " : " + str(decisions[k][i]))
                break
    print("Total Inconsistencias: " + str(countDiff))
    return countDiff


'''
plotLogsReplica(): plot state of each replica in one graph
input: decisions is a list of lists. Each list represents the state of a replica over a period of operations.
'''
def plotStateReplica(decisions):
    # Generate array of float values for each replica
    stateReplicas = []
    operationsReplicas = []
    for replica in decisions:
        stateReplica = [float(i) for i in replica]
        listOperations = list(range(len(replica)))
        stateReplicas.append(stateReplica)
        operationsReplicas.append(listOperations)

    # Add offset to each replica
    offset = True
    stateReplicasOffset = []
    myoffset = 0
    for stateReplica in stateReplicas:
        stateReplicasOffset.append([state + myoffset for state in stateReplica])
        if offset: myoffset += 0.0006

    # Plot
    # x: Operation number or Unit work ~ state (We can think this like 'time')
    # y: Value of each replica
    mycolors = ['red', 'green', 'blue', 'cyan', 'magenta' ,'yellow', 'black', 'orange', 'purple', 'pink', 'brown', 'gray']
    mymarkers = ['d', 'x', '+', '^', '>', 's', 'o', 'v', '<', 'p', '*', 'h']
    for index, replica in enumerate(stateReplicasOffset):
        plt.scatter(operationsReplicas[index], replica, color=mycolors[index], marker=mymarkers[index], label='Replica ' + str(index))
        plt.plot(operationsReplicas[index], replica, color=mycolors[index])
        # plt.semilogx(operationsReplicas[index], replica)
        # plt.semilogy(operationsReplicas[index], replica)
        # plt.gca().yaxis.set_major_formatter(LogFormatter(base=2))

    # Customize Plot
    plt.xlabel('Número de Operación procesada')
    plt.ylabel('Valor USD-PEN')
    # plt.title('Consistency between replicas')
    plt.legend()

    # Apply log scale to the x-axis
    # plt.xscale('log')
    # plt.xscale('symlog', linthresh=1)
    # Show plot
    plt.show()

'''
plotInconsistencies function generate a bar plot of inconsistencies between replicas
Input: listInconsistencies: is a list of objects where each object is a dictionary with inconsistencies
'''
def plotInconsistencies(listInconsistencies):
    print('Plotting Inconsistencies')
    # Set the width of each bar
    barWidth = 0.35

    requestsWorkload = []  # x axis
    srInconsistencies = []  # bars in y axis
    crInconsistencies = []  # bars in y axis
    for workLoad in listInconsistencies:
        print(workLoad)
        requestsWorkload.append(workLoad['numrequests'])
        srInconsistencies.append(workLoad['inconsistencies'][0])
        crInconsistencies.append(workLoad['inconsistencies'][1])
    
    # Set the x positions of the bars
    res1_x = [x for x in range(len(requestsWorkload))]
    res2_x = [x + barWidth for x in res1_x]

    # Create the plot
    plt.bar(res1_x, srInconsistencies, color=SINSMR_COLOR, width=barWidth, edgecolor='white', label='Sin SMR')
    plt.bar(res2_x, crInconsistencies, color=SMR_RABIA_COLOR, width=barWidth, edgecolor='white', label='SMR Rabia')
    # [x + 1 for x in crInconsistencies]
    # Add text labels on top of each bar
    for i, v1, v2 in zip(res1_x, srInconsistencies, crInconsistencies):
        plt.text(i, v1+0.5, str(v1), ha='center')
        plt.text(i, -120, 'Sin SMR', ha='center')
        plt.text(i+barWidth, v2+1, str(v2), ha='center')
        plt.text(i+barWidth, -120, 'SMR Rabia', ha='center')

    # Add xticks on the middle of the group bars
    plt.xlabel('Operaciones procesadas')
    plt.ylabel('Inconsistencias')
    plt.xticks([r + barWidth / 2 for r in range(len(requestsWorkload))], requestsWorkload)

    #plt.title('Inconsistencies in 3 replicas with 2 clients')
    plt.legend()

    # Show the plot
    plt.show()

    return


def mapLogFiles(isRabiaWorkload, workload_dir):
    # Samples log files
    # Sin Rabia Logs
    # srLogFile50_1 = "logs/sinrabia/t_sample_50_2c/redissvr1.log"
    # Con Rabia Logs
    # crLogFile50_1 = "logs/rabia/t_sample_50/rabiasvr1.log"
    # Map log files
    if isRabiaWorkload:
        logFile1 = RABIA_LOGS_DIR + workload_dir + "/rabiasvr1.log"
        logFile2 = RABIA_LOGS_DIR + workload_dir + "/rabiasvr2.log"
        logFile3 = RABIA_LOGS_DIR + workload_dir + "/rabiasvr3.log"
    else:
        logFile1 = REDIS_LOGS_DIR + workload_dir + "/redissvr1.log"
        logFile2 = REDIS_LOGS_DIR + workload_dir + "/redissvr2.log"
        logFile3 = REDIS_LOGS_DIR + workload_dir + "/redissvr3.log"
    return [logFile1, logFile2, logFile3]

'''
Bar plot of inconsistencies for different workloads
'''
def getPlotInconsistencies(listWorkLoadsDirs):
    ### Count inconsistencies for each technique ###
    listInconsistencies = []
    # BEGIN: read Workloads
    for workLoadDir in listWorkLoadsDirs:
        # No Rabia analysis
        srListFiles = mapLogFiles(False, workLoadDir)
        srDecisions, summary = readLogFiles(srListFiles)
        srTotalInconsistencies = checkConsistency(srDecisions)
        # Using Rabia analysis
        crListFiles = mapLogFiles(True, workLoadDir)
        crDecisions, summary = readLogFiles(crListFiles)
        crTotalInconsistencies = checkConsistency(crDecisions)
        # Append results of workload 50
        listInconsistencies.append({'numrequests': len(srDecisions[0]), 'inconsistencies': (srTotalInconsistencies, crTotalInconsistencies)})
    # END: read Workloads    
    # Plot results
    print("listInconsistencies: ")
    print(listInconsistencies)
    plotInconsistencies(listInconsistencies)


def getPlotStateReplica(isRabiaWorkload, workLoadDir):
    # Map log files
    listLogFiles = mapLogFiles(isRabiaWorkload, workLoadDir)
    decisions, summary = readLogFiles(listLogFiles)
    plotStateReplica(decisions)
    return


# Function to plot throughput vs latency to compare two techniques
def plotThroughputVsLatency():
    # Data for SinRabia
    thr_sr = [668, 1772, 2034, 2133, 2228, 2076, 2010]  # Technique 1 throughput
    lat99p_sr = [2, 8, 8, 14, 16.11, 22.67, 23.87]  # Technique 1 latency

    # Data for ConRabia
    thr_cr = [16.67, 99.75, 388.42, 1156, 1241.08, 1290, 1347.25]  # Technique 2 throughput
    lat99p_cr = [101.22, 77.37, 58.61, 22.89, 24.94, 25.94, 30.51]  # Technique 2 latency

    # Plotting the data with lines
    plt.plot(thr_sr, lat99p_sr, 'o-', color=SINSMR_COLOR, label='Sin SMR')
    plt.plot(thr_cr, lat99p_cr, 'o-', color=SMR_RABIA_COLOR, label='SMR Rabia')
    plt.xlabel('Rendimiento (solicitudes/segundo)')
    plt.ylabel('Latencia percentil 99 (ms)')
    plt.legend()

    # Adding grid lines
    plt.grid(True)

    # Displaying the plot
    plt.show()

# Function to plot clients vs latency to compare two techniques
def plotClientsVsLatency():
    # Data for SinRabia
    clients_sr = [1, 3, 4, 6, 9, 12, 15]  # number of parallel clients Technique 1 
    lat99p_sr = [2, 8, 8, 14, 16.11, 22.67, 23.87]  # latencies for Technique 1

    # Data for ConRabia
    clients_cr = [1, 3, 4, 6, 9, 12, 15]  # number of parallel clients Technique 2 
    lat99p_cr = [101.22, 77.37, 58.61, 22.89, 24.94, 25.94, 30.51]  # latencies for Technique 1

    # Plotting the data with lines
    plt.plot(clients_sr, lat99p_sr, 'o-', color=SINSMR_COLOR, label='Sin SMR')
    plt.plot(clients_cr, lat99p_cr, 'o-', color=SMR_RABIA_COLOR, label='SMR Rabia')
    plt.xlabel('Clientes en paralelo')
    plt.ylabel('Latencia percentil 99 (ms)')
    plt.legend()

    # Adding grid lines
    plt.grid(True)

    # Displaying the plot
    plt.show()



def main():
    
    '''
    # Make list of log files
    srListFiles = [srLogFile1, srLogFile2, srLogFile3]
    # Read log files
    decisions, summary = readLogFiles(srListFiles)
    #printSummaryResults(decisions, summary)
    srTotalInc = checkConsistency(decisions)
    plotStateReplica(decisions)
    '''

    
    # Plot State Replicas
    '''
    srWorkLoad = "t_50_2c"
    getPlotStateReplica(False, srWorkLoad)

    crWorkLoad = "t_50_2c"
    getPlotStateReplica(True, crWorkLoad)
    
    # Plot Number of Inconsistencies
    listWorkLoadsDirs = ["t_50_2c", "t_500_2c", "t_5000_2c"]
    getPlotInconsistencies(listWorkLoadsDirs)
    '''
    plotThroughputVsLatency()
    plotClientsVsLatency()
    print("done...bye!")


if __name__ == "__main__":
    main()
