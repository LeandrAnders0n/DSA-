#Question:Isomorphic Strings

# Given two strings s and t, determine if they are isomorphic.
# Two strings s and t are isomorphic if the characters in s can be replaced to get t.
# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

#Appraoach:Create a character mapping from s to t and verifies that all occurrences of each character in s are replaced with corresponding characters from t, while preserving order and ensuring no two characters map to the same character. Return True if the strings are isomorphic, otherwise False.


# Time Complexity & Space Complexity: O(N)

def is_isomorphic(s, t):
    if len(s) != len(t):
        return False

    char_map = {}  

    for i in range(len(s)):
        if s[i] in char_map:
            if char_map[s[i]] != t[i]:
                return False
        else:
            if t[i] in char_map.values():
                return False
            char_map[s[i]] = t[i]

    return True

#Input
s1, t1 = "egg", "add"
s2, t2 = "foo", "bar"
s3, t3 = "paper", "title"

print(is_isomorphic(s1, t1))  # Output: True
print(is_isomorphic(s2, t2))  # Output: False
print(is_isomorphic(s3, t3))  # Output: True

