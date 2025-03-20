'''
Radix sort is a non-comparative sorting algorithm that sorts data by grouping individual digits (or sometimes characters/letters) that share the same significant position and value. It works by processing each digit of an integer or string representation of elements in a list, starting from the least significant digit to the most significant.

Radix sort can be implemented in two ways: LSD (Least Significant Digit) and MSD (Most Significant Digit). The LSD radix sort starts sorting from the rightmost position, which is the least significant digit, while the MSD radix sort starts sorting from the leftmost position, which is the most significant digit.
'''

def radix_sort(myArr):
    max_num = max(myArr)
  
    exp = 1
    while max_num // exp > 0:
        myArr = counting_sort(myArr, exp)
        exp *= 10
  
    return myArr

# helper counting sort function
def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10
  
    # count occurrences of each digit in input array
    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1
  
    for i in range(1, 10):
        count[i] += count[i - 1]
  
    for i in range(n - 1, -1, -1):
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
  
    for i in range(n):
        arr[i] = output[i]
  
    return arr

# Test
myArr = [1,20,50,32,56,0,21]
sorted = radix_sort(myArr)
print('Sorted array: {}'.format(sorted))