#Question: Longest Palindrome
#Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.
# Letters are case sensitive, for example, "Aa" is not considered a palindrome here.
#Approach:Greedy Algorithm
# Count how many times each character appears in the given string. 
# Add up the lengths of all characters that appear an even number of times. 
# Additionally, if there is at least one character that appears an odd number of times, it adds one to the total length. 
# This gives us the length of the longest possible palindrome that can be formed using the characters in the string.
# Time complexity: O(n)
# Space complexity is O(k), where k is the number of unique characters in the string.

def longest_palindrome(str):
    char_count={}
    odd_count=0

    for char in str:
        char_count[char]=char_count.get(char,0)+1
    
    for count in char_count.values():
        if count %2!=0:
            odd_count+=1
    
    longest_palindrome=len(s)-odd_count+(odd_count>0)

    return longest_palindrome








s = "abccccdd"
# Expected Output: 7
print(longest_palindrome(s))