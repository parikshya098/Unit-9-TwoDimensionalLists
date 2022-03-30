def find_row(size):
    first_row = []
    for i in range(size):
        if i == 0 or i == size-1:
            first_row.append('+')
        else:
            first_row.append('-')
    return first_row

n = int(input('Enter size: '))
size = n + 2
l = []
l.append(find_row(size))

for i in range(1, size-1):
    column = []
    for j in range(size):
        if j==0 or j==size-1:
            column.append('|')
        else:
            if(i % 2 == 0):
                if(j % 2 == 0):
                    column.append(' ')
                else: 
                    column.append('*')
            else:
                if(j % 2 == 0):
                    column.append('*')
                else: 
                    column.append(' ')
    l.append(column)
l.append(find_row(size))

o = ""
for i in range(size):
    o += ''.join(l[i])
    o += '\n'
print(o)