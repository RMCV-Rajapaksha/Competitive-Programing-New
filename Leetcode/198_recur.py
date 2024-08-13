class Solution:
    def rob(self, nums: List[int]) -> int:
        #recursive solution
        n =len(nums)
        def helper(i):
            if i==0:
                return nums[0]
            if i==1:
                return max(nums[0],nums[1])

            return max(nums[i]+helper(i-2),helper(i-1))

        return helper(n-1)