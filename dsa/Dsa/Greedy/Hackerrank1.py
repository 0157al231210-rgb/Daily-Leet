#Minimum Absolute Difference in an Array

def minimumAbsoluteDifference(arr):
    arr.sort()
    minDiff = float('inf')
    for i in range(1,len(arr)):
        minDiff = min(minDiff, abs(arr[i -1] - arr[i]))
    return minDiff