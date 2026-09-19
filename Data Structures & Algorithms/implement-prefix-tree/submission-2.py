class PrefixTree:

    def __init__(self):
        self.val = None
        self.nextChars = {}

    def insert(self, word: str) -> None:
        chars = self.nextChars
        c = word[0]
        i = 0

        while c in chars: 
            chars = chars[c].nextChars
            i+= 1
            if i == len(word):
                chars[""] = None
                break
            else: 
                c = word[i]

        # Now, we are in new territory
        while i < len(word): 
            tree = PrefixTree()
            tree.val = word[i]
            c = word[i]
            chars[c] = tree
            chars = tree.nextChars

            i+=1

        chars[""] = None


    def search(self, word: str) -> bool:
        chars = self.nextChars
        i = 0

        while i < len(word): 
            c = word[i]
            if c not in chars: 
                return False
            
            chars = chars[c].nextChars
            i+=1

        if "" in chars:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        chars = self.nextChars
        i = 0

        while i < len(prefix): 
            c = prefix[i]
            if c not in chars: 
                return False
            
            chars = chars[c].nextChars
            i+=1

        return True
        
        