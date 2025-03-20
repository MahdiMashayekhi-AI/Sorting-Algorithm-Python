'''
Selection sort is a simple and intuitive sorting algorithm that works by repeatedly finding the minimum element from an unsorted list and moving it to the beginning of the list. It starts by selecting the smallest element from the entire list and swapping it with the element in the first position. Then, it finds the second-smallest element from the remaining list (excluding the first element), and swaps it with the element in the second position. This process continues until the entire list is sorted.

Selection sort has a time complexity of O(n^2), where n is the number of elements in the list. This makes it less efficient than other sorting algorithms like merge sort and quicksort, both of which have average-case time complexities of O(n log n). However, selection sort has the advantage of requiring only a small amount of additional memory space, making it useful for situations where memory is limited.
'''

def selection_sort(myArr):
    n = len(myArr)

    for i in range(n):
        minIndex = i
        for j in range(i+1, n):
            if myArr[j] < myArr[minIndex]:
                minIndex = j

        myArr[i], myArr[minIndex] = myArr[minIndex], myArr[i]
    
    return myArr

# Test
myArr = [1,20,50,32,56,0,21]
sorted = selection_sort(myArr)
print('Sorted array: {}'.format(sorted))