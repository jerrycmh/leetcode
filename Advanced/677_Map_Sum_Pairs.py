class MapSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.pair = {}

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        self.pair[key] = val
        

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        result = 0
        for key in self.pair.keys():
            for i in range(len(key)+1):
                if prefix == key[:i]:
                    result += self.pair[key]
        return result


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)