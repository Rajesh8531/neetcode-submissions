class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache = {}
        for i,num in enumerate(nums):
            another_num = target-num
            if another_num in cache:
                return sorted([cache[another_num],i])
            cache[num] = i
        return [-1,-1]
        