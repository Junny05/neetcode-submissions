class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c:set() for w in words for c in w}
        for i in range(len(words)-1):
            word1, word2 = words[i],words[i+1]
            minlen = min(len(word1),len(word2))
            if len(word1) > len(word2) and word1[:minlen] == word2[:minlen]:
                return ""
            for j in range(minlen):
                if word1[j] != word2[j]:
                    adj[word1[j]].add(word2[j])
                    break
            # The first letter where they differ is smaller in a than in b.
            # a is a prefix of b and a.length < b.length.

        visited = {}
        res = []

        def dfs(char):
            if char in visited:
                return visited[char]
            
            visited[char] = True

            for i in adj[char]:
                if dfs(i):
                    return True
            visited[char] = False
            res.append(char)

        for char in adj:
            if dfs(char):
                return ""

        res.reverse()
        return "".join(res)