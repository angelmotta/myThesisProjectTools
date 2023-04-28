import csv
import itertools
import matplotlib.pyplot as plt

"""readLogfiles:
Input: two path filenames ideally inside a 'logs' directory placed in the current directory
Output: a 2D array including an array for each replica
"""
def readLogFiles(logfile1, logfile2):
    zip_longest = itertools.zip_longest
    f1 = open(logfile1)
    f2 = open(logfile2)
    csv_f1 = csv.reader(f1, delimiter=" ")
    csv_f2 = csv.reader(f2, delimiter=" ")

    countDiff = 0
    cmdNum = 0
    line = 0
    decisionsR1 = []
    for rowf1, rowf2 in zip_longest(csv_f1, csv_f2):
        line += 1
        if len(rowf1) <= 1: continue    # Blank line [] or ['OK']
        if rowf1[3] == "hello" or rowf1[3] == "ping": continue
        # Assume file only has set commands (0-5 fields)
        decisionsR1.append(rowf1[5])
        if rowf1[5] != rowf2[5]:
            countDiff += 1
            print("Difference at operation #" + str(cmdNum) + ": " + rowf1[5] + " , " + rowf2[5])
        cmdNum += 1

    f1.close()
    f2.close()
    print("Total Commands: " + str(cmdNum))
    print("Total Inconsistencias: " + str(countDiff))
    return decisionsR1


def plotData(decisionsR1):
    print("decisionsR1:")
    print(decisionsR1)
    # TODO: compare len of decisions array between each other
    slotDecisionsR1 = list(range(len(decisionsR1)))
    decisionsR1Fl = [float(i) for i in slotDecisionsR1]
    
    # Create plot
    plt.plot(slotDecisionsR1, decisionsR1Fl)
    plt.xlabel('Slot Decision')
    plt.ylabel('Value USD-PEN')
    plt.title('Consistency over Time between replicas')

    # Plot the data
    # fig, ax = plt.subplots()
    # ax.plot(slotDecisionsR1, decisionsR1)

    # # Reduce the number of values on the y-axis
    # yticks = np.linspace(np.floor(np.min(y)), np.ceil(np.max(y)), 5)
    # ax.set_yticks(yticks)

    # # Show plot
    # plt.show()


def main():
    logfile1 = "logs/sinrabia/redis_svr1.txt"
    logfile2 = "logs/sinrabia/redis_svr2.txt"
    decisionsR1 = readLogFiles(logfile1, logfile2)
    plotData(decisionsR1)
    print("done...bye!")

if __name__ == "__main__":
    main()
