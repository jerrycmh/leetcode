class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
		# Follow the idea of this textbook: http://interactivepython.org/courselib/static/pythonds/Graphs/ImplementingBreadthFirstSearch.html
        
		# exclude special cases
        if endWord not in wordList:
            return 0
        
        # construct bucket
        bucket={}
        for word in wordList+[beginWord]:
            for i in range(len(word)):
                bucketLabel=word[:i]+"_"+word[i+1:]
                try:
                    bucket[bucketLabel].append(word)
                except:
                    bucket[bucketLabel]=[word]
        
        # Tips: if a node will be visited, it will be visited by the shortest path first.
		# So when we update the current wordlist, we can exclude the visited nodes during iteration.
        # if we can find the word set in next step
        # if None, return 0
        # if find endword, return count
		 
        CurrentWordList=set([beginWord])
        visited=set()
       
        count=1
		
        while CurrentWordList:
            tempList=set()
            count+=1
            
            for word in CurrentWordList:
                for i in range(len(word)):
                    bucketLabel=word[:i]+"_"+word[i+1:]
                    if bucketLabel in visited: continue
                    else:
                        visited.add(bucketLabel)
                        tempList.update(bucket[bucketLabel])
            
            if endWord in tempList: return count
            CurrentWordList=tempList
        return 0