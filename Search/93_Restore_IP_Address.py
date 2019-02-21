class Solution:
    def restoreIpAddresses(self, s: 'str') -> 'List[str]':
        if not s:
            return []
        res = []
        self.dfs(s, 0, "", res)
        return res
    
    def dfs(self, s, index, cur_str, res):
        if index == 4:
            if not s and cur_str not in res:
                res.append(cur_str[:-1])
            return
        
        for i in range(1, 4):
            if i <= len(s):
                if i == 1:
                    self.dfs(s[i:], index+1, cur_str+s[:i]+'.',res)
                if i == 2 and s[0] != '0':
                    self.dfs(s[i:], index+1, cur_str+s[:i]+'.', res)
                if i == 3 and s[0] != '0' and int(s[:i]) < 256:
                    self.dfs(s[i:], index+1, cur_str+s[:i]+'.', res)