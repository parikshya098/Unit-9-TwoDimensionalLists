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
            
# reading the values in the file NumbersList.txt into a two dimensional array
with open('NumbersList.txt') as file:
    lines = file.readlines()
    list_nums = []   # a two dimensional array
    for lin in lines:
        # removing spaces and coverting the numbers into integer
        nums = [int(x) for x in lin.strip().split()]
        # append as a list to make it a two dimensional array
        list_nums.append(nums)
    
    # print  the list by calling print_list(a).
    print_list(list_nums)
    # scale factor.
    scale = int(input('Enter scale value: '))
    # calling scaled_list(a, s).
    scaled_list(list_nums,2)
    # calling print_list(a)
    print_list(list_nums)