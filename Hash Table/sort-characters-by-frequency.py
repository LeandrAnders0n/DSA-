#Question:451. Sort Characters By Frequency
# Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.
# Return the sorted string. If there are multiple answers, return any of them.

#Approach:
# Use a dictionary to count the occurrences of each character in s. Then sort the characters based on their counts, and the result string is constructed by repeating each character according to its count. 

# Time complexity: O(n log n), where n is the length of the input string `s` due to the sorting operation.
# Space complexity: O(n), where n is the number of unique characters in the input string `s` stored in the `char_counts` dictionary.

class Solution:
    def frequencySort(self, s: str) -> str:
        char_counts = {}
        result = ""

        for c in s:
            char_counts[c] = char_counts.get(c, 0) + 1

        sorted_chars = sorted(char_counts, key=lambda c: char_counts[c], reverse=True)
        result = ''.join(c * char_counts[c] for c in sorted_chars)

        return result

sol=Solution()
# Example 1:
s = "tree"
print(sol.frequencySort(s))
# Expected Output: "eert"
# Explanation: 'e' appears twice while 'r' and 't' both appear once.
# So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.

# Example 2:
s = "cccaaa"
print(sol.frequencySort(s))
# Expected Output: "aaaccc"
# Explanation: Both 'c' and 'a' appear three times, so both "cccaaa" and "aaaccc" are valid answers.
# Note that "cacaca" is incorrect, as the same characters must be together.

# Example 3:
s = "Aabb"
print(sol.frequencySort(s))
# Expected Output: "bbAa"
# Explanation: "bbaA" is also a valid answer, but "Aabb" is incorrect.
# Note that 'A' and 'a' are treated as two different characters.