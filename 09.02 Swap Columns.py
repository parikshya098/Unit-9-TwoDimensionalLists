import os#importing os module
def print_list(a):#defining print_list function
   for i in range(len(a)):#for loop till length of a
       for j in range(len(a[i])):#for loop till length of a[i]
                      print(a[i][j],end=' ')#printing a[i][j]
       print('\n')#printing new line
def swap_columns(a,i,j):#definition function swap_columns
   for k in range(len(a)):#loop till length of a
       l=a[k][i]#storing a[k][i] in l
       a[k][i]=a[k][j]#storing a[k][j] in a[k][i]
       a[k][j]=l#changing a[k][j] with l
k=open('09.02 NumbersList.txt')#opening the file
a=k.readlines()#reading all the lines
a=''.join(a)#joining the list
a=a.split('\n')#spliting with '\n'
for i in range(len(a)):#for loop till length of a
   a[i]=a[i].split(' ')#spliting the a[i] with space
   a[i]=map(int,a[i])#making each element of a[i] as int
   a[i]=list(a[i])#getting list of mapped function
print_list(a)#calling print_list function 
i,j=input('Enter the columns to swap: ').split()#asking user for columns
i=int(i)#converting to int
j=int(j)#converting to int
swap_columns(a,i,j)#calling swap_columns function 
print_list(a)#calling print_list function