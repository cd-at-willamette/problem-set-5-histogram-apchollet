##################################################
# Name: Aly Chollet
# Collaborators:
# Estimate of time spent (hr):2 
##################################################

def is_magic_square(array:list[list[int]]) -> bool:
    row1 = 0
    row2 = 0
    row3 = 0
    is_magic = 0

    for row in small:
        if sum(row) == 15:
            is_magic += 1
        row1 += row[0]
        row2 += row[1]
        row3 += row[2]
        if row1 == 15:
            is_magic += 1
        if row2 == 15:
            is_magic += 1
        if row3 == 15:
            is_magic += 1
    if sum(small[i][i] for i in range(3)):
        is_magic += 1
    if sum(small[i][2-i] for i in range(3)):
        is_magic += 1
    if is_magic == 8:
        return True
    else:
        return False

small = [[8,1,6,],[3,5,7],[4,9,2]]
print(is_magic_square(small))



