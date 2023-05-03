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
    decisionsR2 = []
    for rowf1, rowf2 in zip_longest(csv_f1, csv_f2):
        line += 1
        if len(rowf1) <= 1: continue    # Blank line [] or ['OK']
        if rowf1[3] == "hello" or rowf1[3] == "ping": continue
        # At the moment assume file only has set commands (0-5 fields)
        decisionsR1.append(rowf1[5])
        decisionsR2.append(rowf2[5])
        if rowf1[5] != rowf2[5]:
            countDiff += 1
            print("Difference at operation #" + str(cmdNum) + ": " + rowf1[5] + " , " + rowf2[5])
        cmdNum += 1

    f1.close()
    f2.close()
    print("Total Commands: " + str(cmdNum))
    print("Total Inconsistencias: " + str(countDiff))
    return decisionsR1, decisionsR2


'''
def plotDatav1(decisionsR1):
    print("decisionsR1:")
    print(decisionsR1)
    # TODO: compare len of decisions array between each other
    slotDecisionsR1 = list(range(len(decisionsR1)))
    decisionsR1Fl = [float(i) for i in decisionsR1]

    # Create plot
    plt.plot(slotDecisionsR1, decisionsR1Fl)
    plt.xlabel('Operation number')
    plt.ylabel('Value USD-PEN')
    plt.title('Consistency between replicas')

    # Show plot
    plt.show()
'''


def plotData(decisionsR1, decisionsR2):
    print("decisionsR1:")
    print(decisionsR1)
    # TODO: compare len of decisions array between each other
    slotDecisionsR1 = list(range(len(decisionsR1)))
    decisionsR1Fl = [float(i) for i in decisionsR1]
    print("decisionsR1 Floats:")
    print(decisionsR1Fl)

    slotDecisionsR2 = list(range(len(decisionsR2)))
    decisionsR2Fl = [float(i) for i in decisionsR2]

    if len(slotDecisionsR1) != len(slotDecisionsR2):
        print("My Panic: len(decisions) are different!")

    # Create plot
    # x: Unit works ~ slotDecisions (We can think this like 'time')
    # y: Value of each replica
    plt.plot(slotDecisionsR1, decisionsR1Fl, label='Replica 1')
    plt.plot(slotDecisionsR2, decisionsR2Fl, label='Replica 2')

    # Customize Plot
    plt.xlabel('Operation number')
    plt.ylabel('Value USD-PEN')
    plt.title('Consistency between replicas')
    plt.legend()

    # Show plot
    plt.show()


def main():
    logfile1 = "logs/sinrabia/redis_svr1.txt"
    logfile2 = "logs/sinrabia/redis_svr2.txt"
    decisionsR1, decisionsR2 = readLogFiles(logfile1, logfile2)
    plotData(decisionsR1, decisionsR2)
    print("done...bye!")

if __name__ == "__main__":
    main()
