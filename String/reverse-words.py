#Question: Reverse Words in a String
# Given an input string s, reverse the order of the words.
# A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.
# Return a string of the words in reverse order concatenated by a single space.
# Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

#Approach:
# Convert the input string to a mutable list. Reverse the entire list to reverse the order of characters in the string. Then, individually reverse each word's characters by tracking word boundaries using two pointers. Reverse the last word separately. Finally, join the reversed characters back into words and adjust spacing to return the reversed string.

#Time Complexity: O(n)
#Space Complexity: O(1)

def reverse_words(s):
    def reverse_range(start, end):
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1
    
    s = list(s.strip())  # Convert to list to make it mutable
    n = len(s)
    
    # Reverse the entire string
    reverse_range(0, n - 1)
    
    start = 0
    for end in range(n):
        if s[end] == ' ':
            reverse_range(start, end - 1)  # Reverse the word
            start = end + 1
    
    # Reverse the last word
    reverse_range(start, n - 1)
    
    # Adjust spacing between words
    return ' '.join(''.join(s).split())





s = "the sky is blue"
print(reverse_words(s))
# Output: "blue is sky the"

s = "  hello world  "
# Output: "world hello"
print(reverse_words(s))

s = "a good   example"
# Output: "example good a"
print(reverse_words(s))
