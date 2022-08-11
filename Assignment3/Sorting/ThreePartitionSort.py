"""
Haily Nguyen, UCP 2022, Aug 11

Sorting Exercise 1: Three Partition Sort
Given an Array [5, 10, 5, 20, 5, 5, 10], sort them in a single pass.
"""


# Swap function at position i and j
def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


"""
This function partitions the array in three parts
a) a[l..i] contains elements smaller than pivot
b) a[i+1..j-1] contains elements equal the pivot
c) a[j..r] contains all elements greater than pivot 
"""


# 3 partition sort or Dutch National Flag Algorithm
def partition(arr, low, high, i, j):
    # To handle 2 elements
    if high - low <= 1:
        if arr[high] < arr[low]:
            swap(arr, high, low)
        i = low
        j = high
        return

    mid = low
    pivot = arr[high]
    while mid <= high:
        if arr[mid] < pivot:
            swap(arr, low, mid)
            low += 1
            mid += 1
        elif arr[mid] == pivot:
            mid += 1
        elif arr[mid] > pivot:
            swap(arr, mid, high)
            high -= 1

    # update i and j
    i = low - 1
    j = mid  # or high+1


# 3-way partition based quick sort
def quickSort(arr, low, high):
    if low >= high:  # 1 or 0 elements
        return

    i = low
    j = high

    # Note that i and j are passed as reference
    partition(arr, low, high, i, j)

    # Recurse two halves
    quickSort(arr, low, i)
    quickSort(arr, j, high)
    return arr


# Driver code
if __name__ == "__main__":
    arr = [5, 10, 5, 20, 5, 5, 10]

    size = len(arr)
    print(arr)
    print(quickSort(arr, 0, size - 1))
