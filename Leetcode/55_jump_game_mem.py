import functools

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        n=len(nums)
        @functools.lru_cache(None)
        def can_reach(i):
            if i==n-1:
                return True
            if i>=n:
                return False
            if nums[i]==0:
                return False
            for j in range(1,nums[i]+1):
                if can_reach(i+j):
                    return True
            return False
        
        return can_reach(0)