'''
Insertion sort is a simple sorting algorithm that works by iteratively building up a sorted portion of an array until the entire array is sorted. The basic idea behind this algorithm is to divide the original unsorted list into a sorted and an unsorted sub-list. Initially, the sorted sub-list contains only the first element of the original list, while the unsorted sub-list contains the remaining elements.

Then, the algorithm proceeds by iterating over each element in the unsorted sub-list, comparing it with the elements in the sorted sub-list, and inserting it at the correct position in the sorted sub-list. In other words, for each element in the unsorted sub-list, we compare it with the last element in the sorted sub-list. If the current element is smaller, we shift the last element in the sorted sub-list one position to the right and continue the comparison until we find the correct position to insert the current element.
'''

def insrtion_sort(myArr):
    for i in range(1, len(myArr)):
        key = myArr[i]

        j = i-1
        while j >= 0 and key < myArr[j]:
            myArr[j+1] = myArr[j]
            j -= 1
        myArr[j+1] = key
    return myArr

# Test
myArr = [1,20,50,32,56,0,21]
sorted = insrtion_sort(myArr)
print('Sorted array: {}'.format(sorted))