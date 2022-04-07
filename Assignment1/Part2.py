"""
Haily Nguyen, UCP 2022, Mar 11

Part 2:
1. isStringPermutation(...)
Implement the function isStringPermutation() that takes two Strings as parameters and
returns a Boolean denoting whether the first string is a permutation of the second string.
"""
from collections import Counter


# The key here is trying to store dictionaries of letters in the string with their frequency
# then compare these 2 dictionaries.
# Time complexity O(n) where n is the length of the string
# Space complexity O(n) where n is the length of the string
def isStringPermutation(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False
    frequency_s1 = Counter(s1)
    frequency_s2 = Counter(s2)
    if frequency_s1 == frequency_s2:
        return True
    return False


print(isStringPermutation("asdf", "fsda"))
print(isStringPermutation("asdf", "fsa"))
print(isStringPermutation("asdf", "fsax"))

# Additional cases
print(isStringPermutation("aaaa", "aaaa"))
print(isStringPermutation("abba", "abbb"))
print(isStringPermutation("!*a", "a*!"))


"""
2. pairsThatEqualSum(...)
Implement the function pairsThatEqualSum() that takes an array of integers and a target 
integer and returns an array of pairs (i.e., an array of tuples) where each pair contains 
two numbers from the input array and the sum of each pair equals the target integer. 
(Order of the output does not matter).
"""

# Time complexity O(n) where n is the length of the string
# Space complexity O(n) where n is the length of the string


def pairsThatEqualSum(inputArray: list, targetSum: int) -> list:
    ans = []
    for i in range(len(inputArray)):
        cur = inputArray[i]
        x = targetSum - cur
        # check if the value x must be another item in the array, or else it wouldn't be a tuple.
        if x in inputArray and (x, cur) not in ans and inputArray.index(x) != i:
            ans.append(tuple((cur, x)))
    return ans


print(pairsThatEqualSum([1, 2, 3, 4, 5], 5))
print(pairsThatEqualSum([1, 2, 3, 4, 5], 1))
print(pairsThatEqualSum([1, 2, 3, 4, 5], 7))


