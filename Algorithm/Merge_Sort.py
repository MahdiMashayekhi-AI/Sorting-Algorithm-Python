'''
Merge sort is a popular sorting algorithm that uses a divide-and-conquer approach. It works by dividing an unsorted array into two halves, sorting each half recursively, and then merging them back together to produce a sorted array.

To implement merge sort, the algorithm first checks if the length of the input array is greater than 1. If so, it divides the array into two halves and sorts each half using a recursive call to merge sort. Once the halves are sorted, the algorithm merges them back together into a single sorted array.
'''

def merge_sort(myArr):
    if len(myArr) > 1:
        mid = len(myArr) // 2
        left = myArr[:mid]
        right = myArr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                myArr[k] = left[i]
                i += 1
            else:
                myArr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            myArr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            myArr[k] = right[j]
            j += 1
            k += 1

    return myArr

# Test
myArr = [1,20,50,32,56,0,21]
sorted = merge_sort(myArr)
print('Sorted array: {}'.format(sorted))
