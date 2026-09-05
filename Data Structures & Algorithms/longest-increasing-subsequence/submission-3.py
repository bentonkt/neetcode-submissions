class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = -1
        memo = []

        def dfs(i): 
            if i == len(nums): 
                return

            num = nums[i]

            if i == 0: 
                memo.append(1)

            else: 
                greatest = 1
                for j in range(i): 
                    if nums[j] < num:
                        # Valid
                        greatest = max(greatest, memo[j] + 1)

                
                memo.append(greatest)

            dfs(i+1)

        dfs(0)

        return max(memo)