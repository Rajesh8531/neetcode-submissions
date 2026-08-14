class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        solution = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            start = i + 1
            end = len(nums) - 1
            while start < end:
                currSum = nums[start] + nums[end]
                if currSum > -nums[i]:
                    end -= 1
                elif currSum < -nums[i]:
                    start += 1
                else:
                    solution.append([nums[i],nums[start],nums[end]])
                    start += 1
                    end -= 1
                    while start < end and nums[start] == nums[start-1]:
                        start += 1
        return solution
        