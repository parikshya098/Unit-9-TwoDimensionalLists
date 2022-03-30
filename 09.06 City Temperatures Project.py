file1 = open('09.06 CityTemps.txt', 'r')
count = 0
temps = []
while True:
    line = file1.readline()
    if not line:
        break

    line = line.split()
    city = line[0]
    records = line[1:]
    temps.append([city,records])

for row in temps:
    total = 0
    for i in range(len(row[1])):
        total = total + int(row[1][i])
    average = total//len(row[1])
    row[1].append(average)

print("City\tMo\tTu\tWe\tTh\tFr\tSa\tSu\tAvg")

for row in temps:
    print(row[0],end="")
    
    for i in row[1]:
        print("\t{}".format(i),end='')
    print()