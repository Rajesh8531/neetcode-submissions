class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for num in nums:
            counter[num] = counter.get(num,0) + 1

        buckets = [[] for i in range(len(nums)+1)]
        for key,value in counter.items():
            buckets[value].append(key)

        sol = []
        count = 0
        for i in range(len(buckets)-1,0,-1):
            bucket = buckets[i]
            if len(bucket) > 0:
                for n in bucket:
                    if count == k:
                        return sol
                    count += 1
                    sol.append(n)
        return sol