#Question: 208. Implement Trie (Prefix Tree)
# A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.
# Implement the Trie class:
# Trie() Initializes the trie object.
# void insert(String word) Inserts the string word into the trie.
# boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
# boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.

#About Trie:
# A Trie is a tree-like data structure that is used to efficiently store and search for strings or words. In this implementation, each Trie node represents a character, and the structure is built by connecting nodes based on the characters of the words.
# The TrieNode class defines the properties of each node, including a dictionary (children) to store child nodes and a boolean (endOfWord) to indicate if the current node represents the end of a word.
# The Trie class uses a TrieNode (self.root) as the starting point for the Trie. The insert method inserts a word into the Trie, creating new nodes as needed. The search method checks if a complete word exists in the Trie, and the startsWith method determines if a given prefix is present in the Trie.
# Tries are commonly employed in tasks such as spell checking, autocomplete, and efficient storage and retrieval of words or strings. They offer fast lookup times for operations related to words and prefixes. In this implementation, the Trie efficiently organizes and manages a set of words, enabling quick checks for word existence and prefix matches.

class TrieNode:
    def __init__(self):
        self.children={}
        self.endOfWord=False

class Trie:

    def __init__(self):
        self.root=TrieNode()        

    def insert(self, word: str) -> None:
        curr=self.root
        for c in word:
            if c not in curr.children:
                curr.children[c]=TrieNode()
        curr=curr.children[c]
        curr.endOfWord=True

    def search(self, word: str) -> bool:
        curr=self.root
        for c in word:
            if c not in curr.children:
                return False
        curr=curr.children[c]
        return curr.endOfWord


    def startsWith(self, prefix: str) -> bool:
        curr=self.root
        for c in prefix:
            if c not in curr.children:
                return False
        curr=curr.children[c]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)