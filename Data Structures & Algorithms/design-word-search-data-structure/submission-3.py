class WordDictionary:

    def __init__(self):
        self.children = {}
        self.end = False

    def addWord(self, word: str) -> None:

        node = self
        for c in word: 
            if c in node.children:
                node = node.children[c]
            else: 
                tree = WordDictionary()
                node.children[c] = tree
                node = node.children[c]

        node.end = True

    def search(self, word: str) -> bool:
        if len(word) == 0 and self.end:
            return True
        node = self

        for i, c in enumerate(word):
            if c == ".":
                for child in node.children: 
                    if node.children[child].search(word[i+1:]):
                        return True

                return False
            else: 
                if c not in node.children:
                    return False
                else: 
                    node = node.children[c]

        return node.end
        
