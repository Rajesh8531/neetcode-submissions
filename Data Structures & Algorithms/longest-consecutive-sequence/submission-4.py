class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums) == 0:
            return 0
        curr = nums[0]
        streak = 0
        i = 0
        sol = 0
        while i < len(nums):
            if curr != nums[i]:
                streak = 0
                curr = nums[i]
            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            
            streak += 1
            curr += 1
            sol = max(streak,sol)
            i += 1
        return sol
            
        