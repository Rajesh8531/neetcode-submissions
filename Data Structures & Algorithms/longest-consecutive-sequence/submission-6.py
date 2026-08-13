class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        maxStreak = 0
        for num in nums:
            if num-1 not in numSet:
                streak = 0
                curr = num
                while curr in numSet:
                    curr += 1
                    streak += 1
                maxStreak = max(maxStreak,streak)
        return maxStreak
            
        