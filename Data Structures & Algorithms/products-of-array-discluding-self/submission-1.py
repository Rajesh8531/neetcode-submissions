class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_array = [1 for i in range(len(nums))]
        postfix_array = [1 for i in range(len(nums))]
        solution = [1 for i in range(len(nums))]

        for i in range(1,len(nums)):
            prefix_array[i] = prefix_array[i-1] * nums[i-1]

        for i in range(len(nums)-2,-1,-1):
            postfix_array[i] = postfix_array[i+1] * nums[i+1]

        for i in range(len(nums)):
            solution[i] = postfix_array[i] * prefix_array[i]

        return solution

        