#Question:433. Minimum Genetic Mutation
# A gene string can be represented by an 8-character long string, with choices from 'A', 'C', 'G', and 'T'.
# Suppose we need to investigate a mutation from a gene string startGene to a gene string endGene where one mutation is defined as one single character changed in the gene string.
# For example, "AACCGGTT" --> "AACCGGTA" is one mutation.
# There is also a gene bank bank that records all the valid gene mutations. A gene must be in bank to make it a valid gene string.
# Given the two gene strings startGene and endGene and the gene bank bank, return the minimum number of mutations needed to mutate from startGene to endGene. If there is no such a mutation, return -1.
# Note that the starting point is assumed to be valid, so it might not be included in the bank.

#Approach:
# The approach utilizes breadth-first search (BFS) to explore possible gene mutations. Genes are represented as 8-character strings, with each mutation defined as a single character change. The algorithm iteratively explores valid mutations from the starting gene to the target gene, maintaining a queue of gene states and their corresponding mutation counts. 

# Time complexity is O(N * L^2), where N is the number of genes in the bank and L is the length of each gene
# Space complexity is O(N)

from typing import List
from collections import deque

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        if not endGene:
            return -1
        
        queue=deque([(startGene,0)])
        bank=set(bank)

        while queue:
            current_gene,mutations=queue.popleft()

            if current_gene==endGene:
                return mutations

            for i in range(len(current_gene)):
                for char in "ACGT":
                    if char !=current_gene[i]:
                        next_gene=current_gene[:i]+char+current_gene[i+1:]
                        if next_gene in bank:
                            bank.remove(next_gene)
                            queue.append((next_gene,mutations+1))
        return -1
 



s=Solution()
# Example 1:
startGene = "AACCGGTT"
endGene = "AACCGGTA"
bank = ["AACCGGTA"]
print(s.minMutation(startGene,endGene,bank))
# Expected Output: 1

# Example 2:
startGene = "AACCGGTT"
endGene = "AAACGGTA"
bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
print(s.minMutation(startGene,endGene,bank))
# Expected Output: 2