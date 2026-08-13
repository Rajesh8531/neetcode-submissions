class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        solutions = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            start = i + 1
            end = len(nums) - 1
            target = -1 * nums[i]
            while start < end:
                total = nums[start] + nums[end]
                if target == total:
                    solutions.append([nums[i],nums[start],nums[end]]) 
                    start += 1
                    end -= 1
                    while start < end and nums[start] == nums[start-1]:
                        start += 1
                elif total < target:
                    start += 1
                else:
                    end -= 1
        return solutions
            
            
        