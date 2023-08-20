#Question: Longest Common Prefix
# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

#Approach:
#It first sorts the list of strings, then compares the characters of the first and last strings in the sorted list, appending matching characters to the ans string. If a character mismatch is found or the loop reaches the end of the shorter string, the function returns the accumulated and.
# Time complexity is O(n * k), where n is the number of strings and k is the length of the shortest  
# Space complexity is O(n), where n is the number of strings.


def longest_common_prefix(strs):
    sorted_s=sorted(strs)
    ans=""
    first=sorted_s[0]
    last=sorted_s[-1]

    for i in range(min(len(first),len(last))):
        if (first[i]!=last[i]):
            return ans
        ans+=first[i]
    return ans


strs = ["dog","racecar","car"]
# Output: ""
print(longest_common_prefix(strs))

strs = ["flower","flow","flight"]
# Output: "fl"
print(longest_common_prefix(strs))