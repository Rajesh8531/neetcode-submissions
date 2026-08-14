class Solution:
    def trap(self, heights: List[int]) -> int:
        left_walls = [0] * len(heights)
        right_walls = [0] * len(heights)

        left_max = heights[0]
        for i in range(len(heights)):
            left_max = max(left_max,heights[i])
            left_walls[i] = left_max

        right_max = heights[len(heights)-1]
        for i in range(len(heights)-1,-1,-1):
            right_max = max(right_max,heights[i])
            right_walls[i] = right_max


        solution = 0
        for i in range(len(heights)):
            current_height = heights[i]
            water_amount = min(right_walls[i],left_walls[i])-current_height
            solution += water_amount
        return solution
        