import csv
import itertools

zip_longest = itertools.zip_longest

f1 = open("./sinrabia/redis_svr1.txt")
f2 = open("./sinrabia/redis_svr2.txt")

csv_f1 = csv.reader(f1, delimiter=" ")
csv_f2 = csv.reader(f2, delimiter=" ")

countDiff = 0
numLine = 1
for rowf1, rowf2 in zip_longest(csv_f1, csv_f2):
    if rowf1 is None or len(rowf1) <= 1:
        # Not SET nor GET could be 'OK' or another command logged
        numLine += 1
        continue
    if rowf1[5] != rowf2[5]:
        countDiff += 1
        print("Difference at operation #" + str(numLine) + ": " + rowf1[5] + " , " + rowf2[5])
    numLine += 1

f1.close()
f2.close()

print("Total Commands: " + str(numLine))
print("Total Inconsistencias: " + str(countDiff))