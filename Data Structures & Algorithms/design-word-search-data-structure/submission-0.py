class TreeNode:
    def __init__(self):
        self.letters = {}
        self.isEnd = False


class WordDictionary:
    def __init__(self):
        self.root = TreeNode()

    def addWord(self, word: str) -> None:
        current = self.root

        for c in word:
            if c in current.letters:
                current = current.letters[c]
            else:
                new_node = TreeNode()
                current.letters[c] = new_node
                current = new_node
        
        current.isEnd = True

    def search(self, word: str) -> bool:
        def dfs(word, node):
            if len(word) == 0:
                return node.isEnd
            
            c = word[0]
            if c == ".":
                for new_node in node.letters.values():
                    if dfs(word[1:], new_node):
                        return True
                return False
            elif c in node.letters:
                return dfs(word[1:], node.letters[c])
            else:
                return False

        return dfs(word, self.root)

