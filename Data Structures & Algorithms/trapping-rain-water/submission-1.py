class Solution:
    def trap(self, nums: List[int]) -> int:
        leftWalls = [0] * len(nums)
        rightWalls = [0] * len(nums)

        solution = 0
        if len(nums) == 0:
            return solution

        maxLeft = nums[0]
        for i in range(len(nums)):
            leftWalls[i] = max(maxLeft,nums[i])
            maxLeft = leftWalls[i]
        
        maxRight = nums[len(nums)-1]
        for i in range(len(nums)-1,-1,-1):
            rightWalls[i] = max(maxRight,nums[i])
            maxRight = rightWalls[i]
        
        for i in range(len(nums)):
            solution += min(leftWalls[i],rightWalls[i]) - nums[i]
        return solution
        