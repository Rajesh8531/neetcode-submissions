class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countMap = defaultdict(int)
        for num in nums:
            countMap[num] += 1

        solution = [(key,value) for key,value in countMap.items()]
        solution = sorted(solution,key = lambda x: x[1])
        solution = [x[0] for x in solution[::-1]]
        
        return solution[:k]
        