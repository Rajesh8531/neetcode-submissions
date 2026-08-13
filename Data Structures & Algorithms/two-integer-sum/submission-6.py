class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            required_number = target - num
            if required_number in seen:
                return [seen[required_number],i]
            seen[num] = i
        return [-1,-1]
        