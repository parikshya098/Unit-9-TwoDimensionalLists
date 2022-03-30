dataline = input("Enter the number of rows and columns: ").split()
m = int(dataline[0])
n = int(dataline[1])
a = []
for i in range(m):
 a.append([0] * n)
for i in range(m):
    dataline= input("Enter a line of a data: ").split() 
    for j in range(n):
        a[i][j] = int(dataline[j])
for i in range (len(a)):
    for j in range(len(a[i])):
     print(a[i][j],end = '') 
    print() 
best_i = 0
best_j = 0
curr_max = a[0][0]   
for i in range(m):
    for j in range(n):
        if a[i][j] > curr_max:
            curr_max = a[i][j]
            best_i = i
            best_j = j
print("The maximum value {} occurred in row {} column {}".format(curr_max,best_i,best_j)) 