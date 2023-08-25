#Question:H-Index
#Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper, return the researcher's h-index.
# According to the definition of h-index on Wikipedia: The h-index is defined as the maximum value of h such that the given researcher has published at least h papers that have each been cited at least h times.

#Approach:
# To calculate the H-Index, sort a list of citation counts in descending order. Check how many citations are greater than or equal to the current position in the sorted list. The highest number where the citation count is at least as large as the position indicates the H-Index. 

#Time Complexity: O(n log n) due to the sorting step
# Space complexity: O(1) 


def h_index(citations):
    n = len(citations)
    citations.sort(reverse=True)  # Sort citations in descending order
    
    h_index = 0
    
    for i, c in enumerate(citations, start=1):
        if c < i:
            break
        h_index = i
    
    return h_index


citations = [3,0,6,1,5]
# Output: 3
print(h_index(citations))

Input: citations = [1,3,1]
# Output: 1
print(h_index(citations))
