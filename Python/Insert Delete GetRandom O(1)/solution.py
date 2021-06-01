import random

class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        numbers = set([])
        self.numbers = numbers

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        try:
            if val in self.numbers:
                raise DuplicateKeyError(f"Value {val} already in {self.numbers}")
            self.numbers.add(val)
            return True
        except:
            return False

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        try:
            self.numbers.remove(val)
            return True
        except:
            return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(tuple(self.numbers))
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

# Your RandomizedSet object will be instantiated and called as such:
obj = RandomizedSet()
param_1 = obj.insert(1)
param_2 = obj.remove(2)
param_3 = obj.insert(2)
param_4 = obj.getRandom()
param_5 = obj.remove(1)
param_6 = obj.insert(2)
param_7 = obj.getRandom()

print(f"""
param_1: {param_1},
param_2: {param_2},
param_3: {param_3}, 
param_4: {param_4},
param_5: {param_5},
param_6: {param_6}, 
param_7: {param_7}
""")