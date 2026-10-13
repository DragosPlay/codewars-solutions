'''
Write an algorithm that takes an array and moves all of the zeros to the end,
preserving the order of the other elements.

move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]
'''

def move_zeros(lst):
    zero_counter = lst.count(0)
    while 0 in lst:
        lst.remove(0)
    for _ in range(zero_counter):
        lst.append(0)
    return lst
