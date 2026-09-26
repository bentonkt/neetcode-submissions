class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:

        nums.sort(reverse=True)
        
        total = sum(nums)
        if total % k != 0: 
            return False

        target = total // k

        subsets = [target] * k

        def dfs(i):
            if i == len(nums): 
                return True

            num = nums[i]

            # choice is what subset to put it in
            prev = -1
            for j, subset in enumerate(subsets): 
                if subset == prev: 
                    continue
                if subset - num < 0:
                    continue
            
                # put it in this one
                subsets[j] -= num
                if dfs(i+1): 
                    return True
                subsets[j] += num

                prev = subset
            # none of the subsets worked
            return False



        return dfs(0)