class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        nei = collections.defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j + 1:]
                nei[pattern].append(word)
                
        visited = set([beginWord])
        q = deque([beginWord])
        res = 1
        while q:
            for i in range(len(q)):
                newword = q.popleft()
                if newword == endWord:
                    return res
                for j in range(len(newword)):
                    pattern = newword[:j] + "*" + newword[j + 1:]
                    for neighbor in nei[pattern]:
                        if neighbor not in visited:
                            q.append(neighbor)
                            visited.add(neighbor)
            res += 1
        return 0 

