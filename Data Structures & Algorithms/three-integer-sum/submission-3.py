class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        solutions = []
        nums.sort()
        seen = set()
        for i in range(len(nums)-2):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            start = i + 1
            end = len(nums) - 1
            target = 0 - nums[i]
            while start < end:
                curSum = nums[start] + nums[end]
                if curSum == target:
                    ans = [nums[i],nums[start],nums[end]]
                    if tuple(ans) not in seen:
                        solutions.append([nums[i],nums[start],nums[end]])
                        seen.add(tuple(ans))
                    end -= 1
                    start += 1
                elif curSum > target:
                    end -= 1
                else:
                    start += 1
        return solutions