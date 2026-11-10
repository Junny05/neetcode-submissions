class TrieNode():
    def __init__(self):
        self.children = [None] * 26
        self.endofword = False

class TrieList():
    def __init__(self):
        self.root = TrieNode()
    
    def addword(self,word):
        curr = self.root

        for s in word:
            index = ord(s) - ord("a")
            if curr.children[index] == None:
                curr.children[index] = TrieNode()
            curr = curr.children[index]
        curr.endofword = True
    
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ROW, COL = len(board), len(board[0])
        visited = set()
        res = set()

        wordbank = TrieList()
        for word in words:
            wordbank.addword(word)
        
        def dfs(r,c,node,path):
            if r >= ROW or c >= COL or r < 0 or c < 0 or (r,c) in visited:
                return
            
            index = ord(board[r][c]) - ord('a')
            if node.children[index] is None:
                return
            node = node.children[index]
            path += board[r][c]
            
            if node.endofword:
                res.add(path)
            
            visited.add((r,c))
            dfs(r-1,c,node,path)
            dfs(r+1,c,node,path)
            dfs(r,c-1,node,path)
            dfs(r,c+1,node,path)
            visited.remove((r,c))

        for r in range(ROW):
            for c in range(COL):
                dfs(r,c,wordbank.root, "")
        return list(res)