"""
Haily Nguyen, UCP 2022, Aug 11

Sorting Exercise 3: Sorted Merge
You are given two sorted arrays, A and B, where A has a large enough buffer at the
end to hold B. Write a method to merge B into A in sorted order in one pass and using O(1) space.
"""

# Time Complexity: O(m+n)
# Space Complexity: O(1)


def sorted_merge(nums_a, m, nums_b, n):
    p1 = m - 1  # end index for array A
    p2 = n - 1  # end index for array B

    # Move p backwards through the array, each time finding
    # the smallest value at p1 or p2.
    for p in range(n + m - 1, -1, -1):
        if p2 < 0:
            break
        if p1 >= 0 and nums_a[p1] > nums_b[p2]:
            nums_a[p] = nums_a[p1]
            p1 -= 1
        else:
            nums_a[p] = nums_b[p2]
            p2 -= 1
    return nums_a


if __name__ == '__main__':
    nums_a = [1, 3, 5, 7, 0, 0, 0, 0, 0]
    m = 4
    nums_b = [2, 4, 6, 8]
    n = len(nums_b)
    print(sorted_merge(nums_a, m, nums_b, n))

