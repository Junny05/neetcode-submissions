class TrieNode():
    def __init__(self):
        self.children = [None] * 26

        self.endOfWord = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root

        for c in word:
            index = ord(c) - ord("a")
            if curr.children[index] == None:
                curr.children[index] = TrieNode()
            curr = curr.children[index]
        curr.endOfWord = True

    def search(self, word: str) -> bool:
        def dfs(node,i):
            if i == len(word):
                return node.endOfWord
            c = word[i]

            if c == '.':
                for child in node.children:
                    if child and dfs(child, i + 1):
                        return True
                return False
            else:
                index = ord(c) - ord("a")
                if not node.children[index]:
                    return False
                return dfs(node.children[index], i+1)
        return dfs(self.root, 0)