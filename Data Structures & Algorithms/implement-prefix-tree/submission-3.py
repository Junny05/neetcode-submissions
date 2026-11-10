class PrefixNode:
    def __init__(self):
        self.children = [None] * 26
        self.endofword = False

class PrefixTree:
    def __init__(self):
        self.root = PrefixNode()

    def insert(self, word: str) -> None:
        curr = self.root

        for w in word:
            index = ord(w) - ord('a')
            if curr.children[index] == None:
                curr.children[index] = PrefixNode()
            curr = curr.children[index]
        curr.endofword = True
    
    def search(self, word: str) -> bool:
        curr = self.root

        for w in word:
            index = ord(w) - ord('a')
            if curr.children[index] == None:
                return False
            curr = curr.children[index]
        return curr.endofword

    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for w in prefix:
            index = ord(w) - ord('a')
            if curr.children[index] == None:
                return False
            curr = curr.children[index]
        return True
        