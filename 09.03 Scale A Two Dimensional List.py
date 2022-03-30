def print_list(a):
    '''
    The function print the list row by row, with one space between each element.
    :params: 'a' a two dimensional list
    '''
    for i in a:
        for j in i:
            print(j, end = ' ')
        print()
        
def scaled_list(a,s):
    '''
     The function that multiplies every value in the list by the scale factor,
    :params: 'a' is a two dimensional list
    :params: 's' is the scale factor
    '''
    for i in range(len(a)):
        for j in range(len(a[i])):
            a[i][j] *= s
            
with open('09.03 NumbersList.txt') as file:
    lines = file.readlines()
    list_nums = []  
    for lin in lines:
        nums = [int(x) for x in lin.strip().split()]
        list_nums.append(nums)
    
    print_list(list_nums)
    scale = int(input('Enter scale value: '))
    scaled_list(list_nums,2)
    print_list(list_nums)