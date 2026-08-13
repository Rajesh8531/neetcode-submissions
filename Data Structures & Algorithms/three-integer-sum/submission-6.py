class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        solutions = []
        nums.sort()
        for i in range(len(nums)-2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i-1] == nums[i]:
                continue
            curr = nums[i]
            start = i+1
            end = len(nums)-1
            target = -1 * curr
            while start < end:
                curSum = nums[start] + nums[end]
                if curSum == target:
                    solutions.append([curr,nums[start],nums[end]])
                    start += 1
                    end -= 1
                    while start < end and nums[start] == nums[start-1]:
                        start += 1
                elif curSum < target:
                    start += 1
                else:
                    end -= 1
        return solutions