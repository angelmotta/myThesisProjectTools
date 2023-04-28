import csv
import itertools

zip_longest = itertools.zip_longest

f1 = open("logs/sinrabia/redis_svr1.txt")
f2 = open("logs/sinrabia/redis_svr2.txt")

csv_f1 = csv.reader(f1, delimiter=" ")
csv_f2 = csv.reader(f2, delimiter=" ")

countDiff = 0
command = 0
line = 0
for rowf1, rowf2 in zip_longest(csv_f1, csv_f2):
    #line += 1
    # print("line #" + str(line))
    # print(rowf1)
    # print(rowf2)
    # print("----")
    if len(rowf1) <= 1:
        # Blank line [] or ['OK']
        continue
    if rowf1[3] == "hello" or rowf1[3] == "ping":
        continue
    # Assume file only has set commands (5 idx fields)
    if rowf1[5] != rowf2[5]:
        countDiff += 1
        print("Difference at operation #" + str(command) + ": " + rowf1[5] + " , " + rowf2[5])
    command += 1

f1.close()
f2.close()

# print("Total Commands: " + str(numLine))
# print("Total Inconsistencias: " + str(countDiff))