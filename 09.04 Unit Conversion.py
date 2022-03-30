
file = open("09.04 Conversion.txt","r")
table = file.readlines()
for l in range(len(table)):
    table[l] = table[l].split(" ")
    if(l != 1):
        for e in table[l][1:]:
            e = float(e)
table[0].insert(0,None)
from_val = float(input("Enter From Value:"))
from_unit = input("Enter From Unit:")
to_unit = input("Enter To Unit:")

flag = 0
from_unit_index = 0
to_unit_index = 0
for i in range(1,len(table)):
    if(table[i][0] == from_unit):
        from_unit_index = i
        flag = 1
        break
if(flag == 1):
    flag = 0
    for i in range(1,len(table[0])):
        if(table[0][i] == to_unit):
            to_unit_index = i
            flag = 1
            break
    if(flag == 1):
        ans = table[from_unit_index][to_unit_index] * from_val
        ans = round(ans,7)
        print(ans)
    else:
        print("ToUnit is not valid")
else:
    print("FromIndex is not valid")