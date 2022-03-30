def swap_columns(a,i,j):
    for k in range(len(a)):
        a[k][i],a[k][j] = a[k][j],a[k][i]
def print_array(a):
    for i in range(len(a)):
        for j in range(len(a[i])):
            print(a[i][j], end = ' ')
        print() 
a = [] 
numbersfile = open("09.02 NumbersList.txt") 
x = numbersfile.readline() 
while x != "":
    y = x.split(" ")
    for i in range(len(y)):
        y[i] = int(y[i])
    a.append(y)  
    x = numbersfile.readline()  
print_array(a)    
rowcolumnsline = input("Enter the columns to swap: ").split()
i = int(rowcolumnsline[0])
j = int(rowcolumnsline[1])
swap_columns(a,  i,   j)
print_array(a)