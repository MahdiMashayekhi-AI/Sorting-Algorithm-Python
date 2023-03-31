'''
The given code implements the Bogo Sort algorithm, which is an extremely inefficient sorting algorithm that sorts an array by repeatedly shuffling the elements randomly until they are sorted.
'''

import random

def bogo_sort(myArr):
    while not is_sorted(myArr):
      shuffle(myArr)
    return myArr

def is_sorted(myArr):
    for i in range(len(myArr) - 1):
        if myArr[i] > myArr[i + 1]:
            return False
    return True

def shuffle(myArr):
    for i in range(len(myArr)):
        j = random.randint(0, len(myArr) - 1)
        myArr[i], myArr[j] = myArr[j], myArr[i]

# Test
myArr = [1,20,50,32,56,0,21]
sorted = bogo_sort(myArr)
print('Sorted array: {}'.format(sorted))
