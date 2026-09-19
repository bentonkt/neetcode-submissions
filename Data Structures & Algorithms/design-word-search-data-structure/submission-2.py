class WordDictionary:

    def __init__(self):
        self.children = {}
        self.end = False

    def addWord(self, word: str) -> None:


        def helper(node, i):
            if i == len(word): 
                return

            c = word[i]
            
            if c in node.children: 
                if i == len(word) - 1:
                    node.children[c].end = True
                else:
                    helper(node.children[c], i+1)
            else: 
                newNode = WordDictionary()
                if i == len(word) - 1:
                    newNode.end = True
                node.children[c] = newNode
                helper(newNode, i+1)

        helper(self, 0)
        

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
        
