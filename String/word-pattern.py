#Question:Word Pattern
# Given a pattern and a string s, find if s follows the same pattern.
# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

#Approach:
# Check if a given pattern of characters matches a given set of words. Start by splitting the input sentence into individual words. If the pattern's length doesn't match the word count, it's a mismatch. Then iterate through the pattern and words simultaneously. Use a dictionary to map characters to words and a set to track used words. If a character is seen again but maps to a different word, or a word is reused, it's a mismatch. Otherwise, the pattern is valid

# Time & Space Complexity: O(N)



def word_pattern(pattern, s):
    words = s.split()
    if len(pattern) != len(words):
        return False
    mapping = {}
    used_words = set()
    for char, word in zip(pattern, words):
        if char in mapping:
            if mapping[char] != word:
                return False
        else:
            if word in used_words:
                return False
            mapping[char] = word
            used_words.add(word)
    return True

pattern = "aaaa"
s = "dog cat cat dog"
# Output: false
print(word_pattern(pattern,s))

pattern = "abba" 
s = "dog cat cat fish"
# Output: false
print(word_pattern(pattern,s))

pattern = "abba" 
s = "dog cat cat dog"
# Output: true
print(word_pattern(pattern,s))
