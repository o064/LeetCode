class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        n = len(beginWord)
        listLength =len(wordList)
        # func to calc if they diff by one 
        def isDiffSingleChar(s1, s2):
            diff = 0
            for a, b in zip(s1, s2):
                if a != b:
                    diff += 1
                    if diff > 1:
                        return False
            return diff == 1
        # adj list fir unidir graph
        adj = defaultdict(list)
        for i in range(listLength):
            for j  in range(i+1 ,listLength ):
                u , v = wordList[i],wordList[j]
                if(isDiffSingleChar(u,v)):
                    adj[u].append(v)
                    adj[v].append(u)
        for i in range(listLength):
            if(isDiffSingleChar(beginWord,wordList[i])):
                adj[beginWord].append(wordList[i])
        # visited dic 
        visited = {w: 0 for w in wordList}
        visited[beginWord] = 1
        # queue for bfs
        q = [(beginWord , 1)]
        # bfs
        while q: 
            u, d =  q.pop(0)
            if u == endWord :
                return d 
            for v in adj[u]:
                if visited[v] == 0:
                    visited[v] = 1
                    q.append((v,d+1))
            visited[u] = 2 
        return 0 

        