class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not numbers:
            return None
        
        mapper = {}
        for i in range(len(numbers)):
            if numbers[i] in mapper:
                return [mapper[numbers[i]]+1, i+1]
            else:
                mapper[target - numbers[i]] = i
        
        return None