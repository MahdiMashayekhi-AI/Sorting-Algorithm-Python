'''
Shell Sort is a sorting algorithm that improves upon the insertion sort algorithm by comparing elements that are spaced apart rather than adjacent. The algorithm works by repeatedly dividing the input array into smaller subarrays and performing an insertion sort on each subarray.

The algorithm begins by defining a gap value g that determines the distance between the elements being compared. Starting with the largest gap, it repeatedly performs an insertion sort on each subarray with a gap of g, until the gap becomes 1. At this point, the algorithm performs one final insertion sort on the entire array to ensure that all elements are in their correct order.
'''

def shell_sort(myArr):
    n = len(myArr)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = myArr[i]
            j = i
            while j >= gap and myArr[j-gap] > temp:
                myArr[j] = myArr[j - gap]
                j -= gap
            myArr[j] = temp
        gap //= 2
    return myArr

# Test
myArr = [1,20,50,32,56,0,21]
sorted = shell_sort(myArr)
print('Sorted array: {}'.format(sorted))