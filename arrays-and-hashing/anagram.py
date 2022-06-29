"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

"""

def isAnagram(s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        freq1 = dict()
        freq2 = dict()
        for letter1, letter2 in zip (s, t):
            if letter1 in freq1:
                freq1[letter1] += 1
            else:
                freq1[letter1] = 1
            if letter2 in freq2:
                freq2[letter2] += 1
            else:
                freq2[letter2] = 1
        
        if freq1 == freq2:
            return True
        else:
            return False


print(isAnagram("anagram", "nagaram"))
print(isAnagram("rat", "car"))