import os
from collections import Counter
""" 
An anagram is a word or phrase formed by rearranging the letters of another word or phrase. 
In other words, two words are anagrams if they contain the same letters, but in a different order.

For example, the words "listen" and "silent" are anagrams because they have the same letters ("l", "i", "s", "t", "e", "n") arranged in different orders. 
Similarly, "debit card" and "bad credit" are anagrams.
"""
os.system('cls' if os.name == 'nt' else 'clear')


# Using the Counter class to count occurrences of the elements
# There is a more accurate checking going on, compared to the set

def is_anagram_using_counter(s: str, t: str) -> bool:
    counter1 = Counter(s)
    counter2 = Counter(t)

    # check if the counters are equal
    return counter1 == counter2

print("This is an anagram checker. Enter 2 words to check if they are anagrams.")
word1 = input("Enter the first word: ")
word2 = input("Enter the second word: ")

if is_anagram_using_counter(word1, word2):
    print(f"{word1} and {word2} are anagrams.")
else:
    print(f"{word1} and {word2} are not anagrams.")

"""
# Check if two strings are anagrams by converting them to sets and comparing both strings.
# The below uses the set data structure
def is_anagram_using_set(s: str, t: str) -> bool:
    set1 = set(s)
    set2 = set(t)

    # check if the sets are equal
    return set1 == set2

print("This is an anagram checker. Enter 2 words to check if they are anagrams.")
word1 = input("Enter the first word: ")
word2 = input("Enter the second word: ")

if is_anagram(word1, word2):
    print(f"{word1} and {word2} are anagrams.")
else:
    print(f"{word1} and {word2} are not anagrams.")

"""