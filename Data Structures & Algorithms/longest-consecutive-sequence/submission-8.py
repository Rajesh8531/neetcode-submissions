class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set()
        lookup = set()
        max_count = 0

        for num in nums:
            lookup.add(num)

        for num in nums:
            if num in seen:
                continue
            count = 0
            curr = num
            while curr in lookup:
                curr += 1
                count += 1
                seen.add(curr)
            max_count = max(count,max_count)

        return max_count