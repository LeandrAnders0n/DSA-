#Question: Group Anagrams
# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

#Approach: Hash Map
# Group the anagrams together using a dictionary. Iterate through each word, sort its characters to create a unique key for anagrams, and store them in the dictionary. Finally, return the grouped anagrams as a list of lists of strings.

# Time Complexity: O(n * k * log(k)), where n is the number of strings in `strs` and k is the maximum length of a string. Sorting each string takes O(k * log(k)) time, and this operation is performed for each of the n strings.
# Space Complexity: O(n * k), where n is the number of strings in `strs`, and k is the maximum length of a string. The space is used to store the dictionary `anagram_groups`, which can have up to n keys, and each key can have a list of strings with a maximum combined length of k.

def group_anagrams(strs):
    group_anagrams={}

    for word in strs:
        sorted_word=''.join(sorted(word))

        if sorted_word in group_anagrams:
            group_anagrams[sorted_word].append(word)
        else:
            group_anagrams[sorted_word]=[word]
    return group_anagrams.values()




strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
print(group_anagrams(strs))

strs = [""]
# Output: [[""]]
print(group_anagrams(strs))

strs = ["a"]
# Output: [["a"]]
print(group_anagrams(strs))