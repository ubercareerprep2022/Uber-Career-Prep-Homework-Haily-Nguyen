"""
Haily Nguyen, UCP 2022, Aug 11

Sorting Exercise 4: Group Anagrams
Write a method to sort an array of strings so that all the anagrams are next to each other.
Assume the average length of the word as “k”, and “n” is the size of the array, where n >> k
(i.e. “n” is very large in comparison to “k”). Do it in a time complexity better than O[n.log(n)]
"""

# Data Structure: Dictionary (Hashmap)
# n words and each word has a maximum of k characters.
# Time Complexity: O(k+n)
# Space Complexity: O(k*n)

from collections import defaultdict


def print_anagrams_together(words):
    grouped_words = defaultdict(list)

    # Put all anagram words together in a dictionary
    # where key is sorted word
    for word in words:
        grouped_words["".join(sorted(word))].append(word)

    for group in grouped_words.values():
        print(" ".join(group))


if __name__ == "__main__":
    arr = ["cat", "dog", "tac", "god", "act"]
    print_anagrams_together(arr)

