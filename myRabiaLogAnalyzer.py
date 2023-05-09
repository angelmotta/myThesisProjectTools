import csv
import itertools

zip_longest = itertools.zip_longest

def readLogFiles(logfile1, logfile2, logfile3):
    f1 = open(logfile1)
    f2 = open(logfile2)
    f3 = open(logfile3)

    csv_f1 = csv.reader(f1, delimiter=" ")
    csv_f2 = csv.reader(f2, delimiter=" ")
    csv_f3 = csv.reader(f3, delimiter=" ")

    countDiff = 0
    numLine = 1
    setCmds = 0
    getCmds = 0
    for rowf1, rowf2, rowf3 in zip_longest(csv_f1, csv_f2, csv_f3):
        numLine += 1
        if len(rowf1) <= 1: continue    # Blank line [] or ['OK']
        if rowf1[3] == "hello" or rowf1[3] == "ping": continue

        # idx '3' is type operation: set | get
        opR1, opR2, opR3 = rowf1[3], rowf2[3], rowf3[3]
        if opR1 != opR2 or opR1 != opR3 or opR2 != opR3:
            print("Tipo Operacion diferente: Op# " + str(numLine))
            countDiff += 1
            continue

        # At this point all replicas have the same kind of operation
        # If operation is Get -> inspect consistency
        if len(rowf1) == 5:
            # Get Command
            getCmds += 1
            # Check key of get operation
            keyR1, KeyR2, KeyR3 = rowf1[4], rowf2[4], rowf3[4]
            if keyR1 != KeyR2 or keyR1 != KeyR3 or KeyR2 != KeyR3:
                print("Operacion GET diferente: Op# " + str(numLine))
                countDiff += 1
                continue
        # If operations is Set -> inspect consistency
        elif len(rowf1) == 6:
            # Set Command
            setCmds += 1
            # Check key of set operation
            keyR1, KeyR2, KeyR3 = rowf1[4], rowf2[4], rowf3[4]
            if keyR1 != KeyR2 or keyR1 != KeyR3 or KeyR2 != KeyR3:
                print("Operacion SET diferente key: Op# " + str(numLine))
                countDiff += 1
                continue
            # Check value of set operation
            valR1, valR2, valR3 = rowf1[5], rowf2[5], rowf3[5]
            if valR1 != valR2 or valR1 != valR3 or valR2 != valR3:
                print("Operacion SET diferente value: Op# " + str(numLine))
                countDiff += 1
                continue
        print(rowf1)
        numLine += 1

    print("Total Sets Commands:" + str(setCmds))
    print("Total Gets Commands:" + str(getCmds))
    print("Total Commands: " + str(getCmds + setCmds))
    print("Total Inconsistencias: " + str(countDiff))

    f1.close()
    f2.close()
    f3.close()
    return

'''
newreadLogFiles: read log files and generate a list of operations executed by each replica
input: list of log files
output: list of operations executed by each replica
'''
def newreadLogFiles(listLogFiles):
    listCsvReaders = []
    for file in listLogFiles:
        f = open(file)
        csvReader = csv.reader(f, delimiter=" ")
        listCsvReaders.append(csvReader)

    countDiff = 0
    numLine = 1
    setCmds = 0
    getCmds = 0
    filesRead = 0
    decisions = []
    for logfile in listCsvReaders:
        decisionReplica = []
        for lineList in logfile:
            # Logic
            # Ignore metadata 
            numLine += 1
            if len(lineList) <= 1: continue    # Blank line [] or ['OK']
            if lineList[3] == "hello" or lineList[3] == "ping": continue
            # If operation is GET (set prev state in decision array for this replica)
            # If operation is SET (set new state in decision array for this replica)
        # Read done, go for next log file
        filesRead += 1
    print("Total read files: " + str(filesRead))


'''
checkConsistency: verify consistency logs finding differences
output: #inconsistencies
'''
def checkConsistency():
    return


'''
plotLogsReplica(): plot state value of each replica in one graph
'''
def plotLogsReplica():
    return


def main():
    logfile1 = "logs/rabia/t4/rabiasvr1log.txt"
    logfile2 = "logs/rabia/t4/rabiasvr2log.txt"
    logfile3 = "logs/rabia/t4/rabiasvr3log.txt"
    #readLogFiles(logfile1, logfile2, logfile3)
    listFiles = [logfile1]
    newreadLogFiles(listFiles)
    #plotData(decisionsR1, decisionsR2)
    print("done...bye!")


if __name__ == "__main__":
    main()
