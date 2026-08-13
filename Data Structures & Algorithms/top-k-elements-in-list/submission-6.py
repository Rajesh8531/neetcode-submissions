class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for _ in range(len(nums)+1)]
        countMap = {}
        for num in nums:
            countMap[num] = countMap.get(num,0) + 1
        for key,value in countMap.items():
            buckets[value].append(key)
        
        res = []
        for i in range(len(nums),0,-1):
            if len(buckets[i]) != 0:
                res.extend(buckets[i])
        return res[:k]
        
        