class TreeNode:
    def __init__(self):
        # Keep a dictionary containing all of the letters coming after this one
        self.suffixes = {}
        self.isEnd = False # Keeps track of whether this letter is the end of a word

class PrefixTree:

    def __init__(self):
        self.root = TreeNode()

    def insert(self, word: str) -> None:
        current = self.root
        for c in word:
            if c in current.suffixes:
                current = current.suffixes[c]
            else: 
                new_node = TreeNode()
                current.suffixes[c] = new_node
                current = new_node
        current.isEnd = True


    def search(self, word: str) -> bool:
        current = self.root
        for c in word:
            if c in current.suffixes:
                current = current.suffixes[c]
            else:
                return False

        return current.isEnd

    def startsWith(self, prefix: str) -> bool:
        current = self.root
        for c in prefix:
            if c in current.suffixes:
                current = current.suffixes[c]
            else:
                return False
        return True
        
        