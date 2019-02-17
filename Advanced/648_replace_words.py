class Solution(object):
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        if not dict or not sentence:
            return ""
        
        roots = set(dict)
        words = sentence.split()
        result = []
        
        for index in range(len(words)):
            word = words[index]
            for i in range(1, len(word)):
                if word[:i] in roots:
                    word = word[:i]
                    break
            result.append(word)
        
        return ' '.join(result)