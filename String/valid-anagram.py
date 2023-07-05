#Question:Valid Anagram
#Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

#Approach: Use Hash Table
# We check if two strings, s and t, are anagrams by comparing the frequency of characters in each string. 
# Create dictionaries s_dict and t_dict to store the character frequencies and then compare the dictionaries to determine if the strings are anagrams.

# Time complexity & Space complexity: O(n)

def valid_anagram(s,t):
    s_dict,t_dict={},{}

    if len(s)!=len(t):
        return False
    for c in s:
        s_dict[c]=s_dict.get(c,0)+1
    for c in t:
        t_dict[c]=t_dict.get(c,0)+1
    
    return s_dict==t_dict


s,t = "rat","car"
# Expected Output: false
print(valid_anagram(s,t))
s,t = "anagram","nagaram"
# Expected Output: true
print(valid_anagram(s,t))