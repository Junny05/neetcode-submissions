class TrieNode():
    def __init__(self):
        self.children = [None] * 26
        self.isEndOfWord = False

class TrieList():
    def __init__(self):
        self.root = TrieNode()
    
    def addWord(self, word):
        curr = self.root

        for c in word:
            index = ord(c) - ord("a")
            if curr.children[index] == None:
                curr.children[index] = TrieNode()
            curr = curr.children[index]
        curr.isEndOfWord = True 
    
    def search(self, word):
        curr = self.root

        for c in word:
            index = ord(c) - ord("a")
            if curr.children[index] == None:
                return False
            curr = curr.children[index]
        return True
    
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        visited = set()
        res = set()
        wordbank = TrieList()

        for word in words:
            wordbank.addWord(word)
        
        def dfs(r,c,node, path):

            if r >= len(board) or c >= len(board[0]) or c < 0 or r < 0 or (r,c) in visited:
                return

            index = ord(board[r][c]) - ord('a')
            if node.children[index] is None:
                return 

            node = node.children[index]
            path += board[r][c]
            if node.isEndOfWord:
                res.add(path)

            visited.add((r,c))
            dfs(r+1,c,node,path)
            dfs(r-1,c, node,path)
            dfs(r,c-1,node,path)
            dfs(r,c+1,node,path)
            visited.remove((r,c))
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                dfs(r, c, wordbank.root,"")
        return list(res)
