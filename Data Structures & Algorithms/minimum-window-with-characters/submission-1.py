class Solution:
    def minWindow(self, s: str, t: str) -> str:
        counts = Counter(t)
        indices = {}
        for c in t: 
            indices[c] = []

        numFound = 0
        foundAll = False

        using = set()

        lenRes = float('inf')
        res = ""

        for i, c in enumerate(s): 
            if c in indices: 

                # Check if we already have the right number
                if len(indices[c]) == counts[c]:
                    indices[c].append(i)

                    using.add(i)
                    using.remove(indices[c].pop(0))
                    if numFound == len(t): 
                        # update minimum
                        minimum = min(using)
                        if i+1 - minimum < lenRes:
                            res = s[minimum:i+1]
                            lenRes = i+1 - minimum

                else:
                    indices[c].append(i)

                    using.add(i)

                    numFound += 1

                    if numFound == len(t): 
                        # update minimum
                        minimum = min(using)
                        if i+1 - minimum < lenRes:
                            res = s[minimum:i+1]
                            lenRes = i+1 - minimum



        return res