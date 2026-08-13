class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache = {}
        for i in range(len(nums)):
            curr = nums[i]
            if target - curr in cache:
                return [cache[target-curr],i]
            cache[curr] = i
        return [-1,-1]
        