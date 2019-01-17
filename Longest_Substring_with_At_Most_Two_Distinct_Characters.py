class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        if len(set(s)) == 1:
            return len(s)
        
        max_len = counter = 0
        queue = []
        mapper = {}
        
        for x in s:
            if len(queue) < 2:
                if x not in queue:
                    queue.append(x)
                    mapper[x] = 1
                else:
                    if x != queue[-1]:
                        queue[0], queue[1] = queue[1], queue[0]
                        mapper[x] == 1
                    else:
                        mapper[x] += 1
                counter += 1
            else:
                if x not in queue:
                    max_len = max(max_len, counter)
                    val = mapper.pop(queue.pop(0))
                    counter = mapper[queue[0]]
                    queue.append(x)
                    mapper[x] = 1
                else:
                    if x != queue[-1]:
                        queue[0], queue[1] = queue[1], queue[0]
                        mapper[x] = 1
                    else:
                        mapper[x] += 1
                counter += 1
        
        return max(max_len, counter)