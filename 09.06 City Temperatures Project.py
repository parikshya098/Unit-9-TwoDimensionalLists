# Using readline()
file1 = open('CityTemps.txt', 'r')
count = 0
temps = []
while True:
    # Get next line from file
    line = file1.readline()
 
    # if line is empty
    # end of file is reached
    if not line:
        break
    
    #split the line with space
    line = line.split()
    #the first word will be city name
    city = line[0]
    #remaining all records will be the temperature values
    #so take a sublist from index 1
    records = line[1:]
    #add the list city,record to the temps list
    temps.append([city,records])

#iterater for each row in temps
for row in temps:
    #declare total as 0
    total = 0
    #iterate through each temperature value in the city
    for i in range(len(row[1])):
        #add the temperature to total
        #since values read from files are of type string
        #to convert it to integer we will use int() function
        total = total + int(row[1][i])
    #find the average
    #// returns only the integeral part of divison
    average = total//len(row[1])

    #append the average to the end of the row
    row[1].append(average)

#print the result
#print the header
print("City\tMo\tTu\tWe\tTh\tFr\tSa\tSu\tAvg")

#iterate through the temps array
for row in temps:
    #row[0] contains the city name so print it
    print(row[0],end="")
    #row[1] contains all the temperature and average
    #so print it one by one
    for i in row[1]:
        print("\t{}".format(i),end='')
    print()