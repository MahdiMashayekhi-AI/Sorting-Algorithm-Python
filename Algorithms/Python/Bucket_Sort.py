'''
he bucket_sort function takes an array myArr as input and returns a sorted version of that array using the Bucket Sort algorithm.

First, the maximum value in the input array is determined and stored in maxValue. A list of empty buckets is then created, with the number of buckets equal to the length of the input array.

Each value in the input array is then assigned to a bucket based on its value. This is done by dividing the value by maxValue and multiplying the result by len(myArr)-1 to get the index of the bucket to which the value should be assigned. The value is then appended to that bucket.
'''

def buccket_sort(myArr):
    maxValue = max(myArr)
    bucket = [[] for _ in range(len(myArr))]

    for value in myArr:
        index = int(value/maxValue * (len(myArr)-1))
        bucket[index].append(value)

    for i in range(len(myArr)):
        bucket[i] = sorted(bucket[i])

    result = []
    for i in range(len(myArr)):
        result.extend(bucket[i])

    return result

# Test
myArr = [1,20,50,32,56,0,21]
sorted = buccket_sort(myArr)
print('Sorted array: {}'.format(sorted))