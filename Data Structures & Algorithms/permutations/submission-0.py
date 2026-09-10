class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        numSet = set(nums)
        def dfs(path, options): 
            nonlocal res
            # print(path)
            # print(options)
            # print("_____")
            if not options: 
                res.append(path.copy())
                return

            for num in options.copy(): 
                options.remove(num)

                path.append(num)

                # print(path)
                # print(options)
                # print("_____")

                dfs(path.copy(), options.copy())
                options.add(num)
                path.remove(num)


            return  

        dfs([], numSet)
        return res
            