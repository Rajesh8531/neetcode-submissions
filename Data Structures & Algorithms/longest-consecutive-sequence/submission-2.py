class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        sol = 0
        for num in nums:
            streak, current = 0, num
            while current in numSet:
                streak += 1
                current += 1
            sol = max(sol,streak)
        return sol
            
        