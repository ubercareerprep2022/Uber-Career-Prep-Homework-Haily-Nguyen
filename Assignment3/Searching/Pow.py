"""
Haily Nguyen, UCP 2022, Aug 11

Searching Exercise 3: Implement pow(x, n)
Implement pow(x, n), which calculates x raised to the power n.
"""


# Time Complexity: O(log n)
# Space Complexity: O(log n)

def repeated_multiplication(base, exp):
    if exp == 0:
        return 1
    intermediate = repeated_multiplication(base, exp // 2)
    if (exp % 2) == 0:
        return intermediate * intermediate
    return intermediate * intermediate * base


def pow(x, n):
    # The repeated_multiplication helper function takes care of n = 0 case

    # Negative case
    if n < 0:
        return 1 / repeated_multiplication(x, n * -1)

    # Positive case
    return repeated_multiplication(x, n)


print(pow(2, 10))
