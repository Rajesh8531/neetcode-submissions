class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for _ in range(len(nums)+1)]
        countMap = {}
        for num in nums:
            if num not in countMap:
                countMap[num] = 0
            countMap[num] += 1
        
        for num, count in countMap.items():
            buckets[count].append(num)
        
        res = []
        for i in range(len(nums),0,-1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res
        return res
        
        