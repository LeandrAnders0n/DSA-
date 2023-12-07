#Question:211. Design Add and Search Words Data Structure
# Design a data structure that supports adding new words and finding if a string matches any previously added string.
# Implement the WordDictionary class:
# WordDictionary() Initializes the object.
# void addWord(word) Adds word to the data structure, it can be matched later.
# bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.

#Approach:
# This code defines a Trie data structure and a WordDictionary class using that trie. The trie nodes represent characters, and the WordDictionary supports adding words and searching for words. The addWord method inserts a word into the trie, and the search method checks if a word exists, allowing for wildcard '.' characters. The search_helper function recursively traverses the trie to match a given word with optional wildcard characters. For each character in the word:
# - If it's a dot ('.'), the function explores all child nodes and continues recursively.
# - If it's a regular character, it checks if it exists in the current node's children.
# The function returns True only if the entire word is matched, and False otherwise.

class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.endOfWord = True

    def search(self, word: str) -> bool:
      return self.search_helper(self.root,word)

    def search_helper(self,node,word:str)->bool:
      curr=node
      for i,c in enumerate(word):
        if c==".":
          for child in curr.children.values():
            if self.search_helper(child,word[i+1:]):
              return True
          return False
        elif c not in curr.children:
          return False
        curr=curr.children[c]
      return curr.endOfWord
  

