class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.graph = {}
        self.arr = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.arr: return False
        else:
            self.arr.append(val)
            self.graph[val] = len(self.arr)-1
            return True
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if not self.arr: return False
        if val not in self.arr: return False
        else:
            index, last = self.graph[val], self.arr[-1]
            self.graph[last] = index
            self.arr[-1], self.arr[index] = self.arr[index], self.arr[-1]
            del self.arr[-1]
            del self.graph[val]
            return True
        

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return self.arr[random.randint(0, len(self.arr)-1)]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()