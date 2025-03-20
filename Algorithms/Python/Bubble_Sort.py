'''
This code implements the bubble sort algorithm to sort an input list of integers. The bubble_sort function takes the input list, myArr, as an argument and first computes its length. It then iterates through the list using two nested loops to compare adjacent elements and swap them if they are in the wrong order. The outer loop iterates over each element of the list, while the inner loop iterates over the elements that haven't been sorted yet. The inner loop range starts from 0 and goes up to the second last element minus the number of elements already sorted in the outer loop.
'''

def bubble_sort(myArr):
    n = len(myArr)

    for i in range(n):
        for j in range(0, n-i-1):
            if myArr[j] > myArr[j+1]:
                myArr[j], myArr[j+1] = myArr[j+1], myArr[j]
    return myArr

# Test
myArr = [1,20,50,32,56,0,21]
sorted = bubble_sort(myArr)
print('Sorted array: {}'.format(sorted))