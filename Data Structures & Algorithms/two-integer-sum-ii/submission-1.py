class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            num = nums[i]
            required_num = target - num
            if required_num in seen:
                return [seen[required_num]+1, i+1]
            seen[num] = i
        return [-1,-1]