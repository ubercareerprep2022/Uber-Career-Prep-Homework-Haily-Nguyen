"""
Haily Nguyen, UCP 2022, Aug 11

Searching Exercise 1: Find Minimum
Write the code to find the minimum element in a rotated and sorted array
"""


# Time Complexity: O(log n)
# Space Complexity: O(1)
# n is the number of elements in array

def find_min(arr, low, high):
    while low < high:
        mid = low + (high - low) // 2

        if arr[mid] == arr[high]:
            high -= 1
        elif arr[mid] > arr[high]:
            low = mid + 1
        else:
            high = mid
    return arr[high]


# Driver program to test above functions
arr1 = [5, 6, 1, 2, 3, 4]
n1 = len(arr1)
print("The minimum element is " + str(find_min(arr1, 0, n1 - 1)))

arr2 = [1]
n2 = len(arr2)
print("The minimum element is " + str(find_min(arr2, 0, n2 - 1)))
