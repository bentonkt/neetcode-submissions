class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        emails = defaultdict(list)
        for i, account in enumerate(accounts): 
            name = account[0]
            for email in account[1:]:
                emails[(name, email)].append(i)

        visited = set()
        def dfs(i):

            if i in visited: 
                return set()

            visited.add(i)
            account = accounts[i]
            name = account[0]

            res = set(account[1:])

            for email in account[1:]:
                neighbors = emails[(name, email)]

                for neighbor in neighbors: 
                    res.update(dfs(neighbor))


            return res

        result = []

        for i in range(len(accounts)): 
            name = [accounts[i][0]]
            val = sorted(list(dfs(i)))

            if len(val) == 0:
                continue
            name.extend(val)
            result.append(name)


        return result
            
            