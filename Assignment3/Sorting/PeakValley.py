"""
Haily Nguyen, UCP 2022, Aug 11

In an array of integers, a "peak" is an element that is greater than or equal to the adjacent
integers and a "valley" is an element that is less than or equal to the adjacent integers.
For example, in the array [5, 8, 6, 2, 3, 4, 6], [8, 6] are peaks and [5, 2] are valleys.
Given an array of integers, sort the array into an alternating sequence of peaks and valleys.

Example
Input: [5, 3, 1, 2, 3]
Output: [5, 1, 3, 2, 3]
"""

# Time Complexity: O(n)
# Space Complexity: O(1)


def alternating_sequence(nums):
    # sort the array in decreasing order
    arr = sorted(nums, reverse=True)
    pos = len(arr) // 2
    # Divide the array into 2 equal halves
    if len(arr) % 2 == 1:
        a = arr[:pos + 1]
        b = arr[pos + 1:]
    else:
        a = arr[:pos]
        b = arr[pos:]
    # reverse the order of these halves
    # we have array a with peak values while array b has valley values
    a, b = a[::-1], b[::-1]
    for i in range(len(nums)):
        pos = i // 2
        # even index for peak number in array a
        if i % 2 == 0:
            nums[i] = a[pos]
        # odd index for valley number in array a
        else:
            nums[i] = b[pos]
    return nums


print(alternating_sequence([5, 3, 1, 2, 3]))