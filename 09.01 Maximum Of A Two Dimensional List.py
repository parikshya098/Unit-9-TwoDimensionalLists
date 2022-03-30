print("Enter the number of rows and columns:")

m = int(input());

n = int(input());

# matrix

matrix = [];

# take input for matrix

for i in range(m):          

    l = [];

    print("Enter a line of data:");

    for j in range(n):      

        l.append(int(input()));

    matrix.append(l);

# print matrix    

for i in range(m):          

    for j in range(n):      

        print(matrix[i][j],end = " ");

    print();

# find max in matrix

max = 0;

for i in range(m):          

    for j in range(n):  

        if max < matrix[i][j]:

            max = matrix[i][j];

# print max

a = 0;

b = 0;

for i in range(m):          

    for j in range(n):  

        if max == matrix[i][j]:

            a = i;

            b = j;

            print("The maximum value",max,"occurred in row",a,"column",b);

            break;