'''
Heap Sort is an efficient sorting algorithm that operates by creating a binary heap data structure from the input array and then using this heap to sort the elements of the array in-place. The binary heap is a complete binary tree that satisfies the heap property: any parent node has a value greater than or equal to that of its children.

The Heap Sort algorithm consists of two main phases. In the first phase, the input array is transformed into a binary heap using a process called "heapify". This involves starting at the last non-leaf node in the heap and working backwards to the root, ensuring that each node satisfies the heap property.
'''

def heap_sort(myArr):
    n = len(myArr)

    for i in range(n // 2-1, -1, -1):
        heapify(myArr, n, i)

    for i in range(n-1, 0, -1):
        myArr[i], myArr[0] = myArr[0], myArr[i]
        heapify(myArr, i, 0)

    return myArr

def heapify(arr, n, i):
    largest = i 
    l = 2 * i + 1
    r = 2 * i + 2   
  
    # See if left child of root exists and is larger than root
    if l < n and arr[largest] < arr[l]:
        largest = l
  
    # See if right child of root exists and is larger than root
    if r < n and arr[largest] < arr[r]:
        largest = r
  
    # Change root, if needed
    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i] # swap
  
        heapify(arr, n, largest)

# Test
myArr = [1,20,50,32,56,0,21]
sorted = heap_sort(myArr)
print('Sorted array: {}'.format(sorted))