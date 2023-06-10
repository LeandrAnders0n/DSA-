# Question:Find the longest common substring of two strings.
#Approach: Find the length of the smaller string, and iterate through both strings comparing elements, if the elements are similar append to the substring array.
#Else return the substring array
# Time complexity: O(n) 
# Space complexity: O(n)

def longest_substring(s1,s2):

    n=min(len(s1),len(s2))
    substring=[]
    for i in range(n):

        if s1[i]==s2[i]:
            substring.append(s1[i])
    return substring



s1=['H','e','l','l','o']
s2=['Y','e','l','l','o','w']
print(longest_substring(s1,s2))