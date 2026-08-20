class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_heap = []
        solution = []
        for i in range(len(nums)):
            num = nums[i]
            heapq.heappush(max_heap, (-num,i))
            if i >= k - 1:
                while max_heap[0][1] <= i - k:
                    heapq.heappop(max_heap)
                solution.append(-max_heap[0][0])
        return solution
        