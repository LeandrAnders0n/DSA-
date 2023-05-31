# Question:Given a string s, find the length of the longest substring without repeating characters.
#Approach: We use a Hash Map and the Sliding Window Algorithm to tackle this question.
# We employ a sliding window approach with a hash table char_map to store characters and their indices. 
# The left pointer indicates the start of the current window. We iterate through the string using the right pointer. 
# If the current character is already in char_map and its index is within the current window (left <= char_map[s[right]]), we update the left pointer to the next position after the repeated character. 
# We update the index of the current character in char_map and the maximum length when a longer non-repeating substring is found.

def longest_substring(s):
    char_map={}
    max_length=0
    left=0

    for right in range(len(s)):

        if s[right] in char_map and left<=char_map[s[right]]:
            left=char_map[s[right]]+1
        
        char_map[s[right]]=right
        max_length=max(max_length,right-left+1)
    
    return max_length



s = "abcabcbb"
print(longest_substring(s))