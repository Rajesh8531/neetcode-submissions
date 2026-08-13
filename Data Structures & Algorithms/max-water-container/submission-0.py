class Solution:
    def maxArea(self, heights: List[int]) -> int:
        highArea = 0
        start = 0
        end = len(heights) - 1
        while start < end:
            startHeight = heights[start]
            endHeight = heights[end]
            area = min(startHeight,endHeight) * (end-start)
            highArea = max(area,highArea)
            if startHeight < endHeight:
                start += 1
            elif startHeight > endHeight:
                end -= 1
            else:
                start += 1
                end -= 1
        return highArea