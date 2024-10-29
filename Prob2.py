##################################################
# Name:
# Collaborators:
# Estimate of time spent (hr):
##################################################

def is_magic_square(array:list[list[int]]) -> bool:
    row1 = 0
    row2 = 0
    row3 = 0
    '''if small[0][0] + small[0][1] + small[0][2] == 15:
        print(True)
    else:
        print(False)'''

    for row in small:
        if sum(row) == 15:
            print('sum row=',sum(row),',True')
        row1 += row[0]
        row2 += row[1]
        row3 += row[2]
        if row1 == 15:
            print("r1= true")
        if row2 == 15:
            print("r2= true")
        if row3 == 15:
            print("r3= true")







    #check if the list is greater than 3, return false






small = [[8,1,6],[3,5,7],[4,9,2]]
print(is_magic_square(small))



