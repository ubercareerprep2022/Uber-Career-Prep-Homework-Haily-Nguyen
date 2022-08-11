"""
Haily Nguyen, UCP 2022, Aug 11

Searching Exercise 2: Find Element
Write the code to find an element in a rotated and sorted array
"""


def find_element(arr, low, high, key):
    if low > high:
        return -1

    mid = (low + high) // 2
    if arr[mid] == key:
        return mid

    # If arr[low...mid] is sorted
    if arr[low] <= arr[mid]:
        # As this subarray is sorted, we can quickly
        # check if key lies in half or other half
        if arr[low] <= key <= arr[mid]:
            return find_element(arr, low, mid - 1, key)
        return find_element(arr, mid + 1, high, key)

    # If arr[low..mid] is not sorted, then arr[mid... r] must be sorted
    if arr[mid] <= key <= arr[high]:
        return find_element(arr, mid + 1, high, key)
    return find_element(arr, low, mid - 1, key)


# Driver
if __name__ == '__main__':
    arr = [2, 3, 6, 7, 10, 3, 1, 2]
    key = 3
    i = find_element(arr, 0, len(arr) - 1, key)
    if i != -1:
        print("Index of element: ", i)
    else:
        print("Element not found")

