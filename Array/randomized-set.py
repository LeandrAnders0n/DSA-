#Question: Insert Delete GetRandom O(1)
# Implement the RandomizedSet class:
# RandomizedSet() Initializes the RandomizedSet object.
# bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
# bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
# int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.
# You must implement the functions of the class such that each function works in average O(1) time complexity.

# Average Time Complexity: O(1)
# Space Complexity: O(1)

import random

class RandomizedSet:

    def __init__(self):
        self.r_set = set()
        self.r_list = []

    def insert(self, val: int) -> bool:
        if val not in self.r_set:
            self.r_set.add(val)
            self.r_list.append(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.r_set:
            self.r_set.remove(val)
            self.r_list.remove(val)
            return True
        return False

    def getRandom(self) -> int:
        if self.r_list:
            return random.choice(self.r_list)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
