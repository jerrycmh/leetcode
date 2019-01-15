class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.queue_keys = []
        self.mapper = {}

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.mapper:
            return -1
        else:
            self.queue_keys.remove(key)
            self.queue_keys.append(key)
            return self.mapper[key]
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if len(self.queue_keys) == self.capacity and key not in self.queue_keys:
            self.mapper.pop(self.queue_keys.pop(0))
        if key in self.mapper:
            self.queue_keys.remove(key)
        self.mapper[key] = value
        self.queue_keys.append(key)