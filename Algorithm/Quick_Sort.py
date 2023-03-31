'''
This is an implementation of the Quick Sort algorithm in Python.
The function takes a list of numbers (myArr) as input and recursively
sorts the list in ascending order.

The algorithm works by selecting a pivot element from the list
(in this implementation, the first element is chosen as the pivot),
and partitioning the list into two sub-lists, one containing
elements less than the pivot and the other containing elements
greater than or equal to the pivot. The two sub-lists are
then sorted recursively using the same process until the entire
list is sorted.
'''

def quick_sort(myArr):
    if len(myArr) <= 1:
        return myArr
    else:
        pivot = myArr[0]
        left = []
        right = []

        for i in range(1, len(myArr)):
            if myArr[i] < pivot:
                left.append(myArr[i])
            else:
                right.append(myArr[i])
        return quick_sort(left) + [pivot] + quick_sort(right)
    
# Test
myArr = [1,20,50,32,56,0,21]
sorted = quick_sort(myArr)
print('Sorted array: {}'.format(sorted))