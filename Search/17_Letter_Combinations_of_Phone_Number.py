class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        
        num_pad = {
            2:"abc",
            3:"def",
            4:"ghi",
            5:"jkl",
            6:"mno",
            7:"pqrs",
            8:"tuv",
            9:"wxyz"
        }
        
        def dfs(digits,letters,index,res):
            if index == len(digits):
                res.append(letters)
                return
            for ch in num_pad[int(digits[index])]:
                dfs(digits, letters+ch, index+1, res)

        result = []
        letters = ""
        dfs(digits, letters, 0, result)
        return result