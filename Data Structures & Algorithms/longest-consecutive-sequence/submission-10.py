class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        lookup = set()
        max_count = 0

        for num in nums:
            lookup.add(num)

        for num in nums:
            if num - 1 in lookup:
                continue
            length = 1
            while num + length in lookup:
                length += 1
            max_count = max(length,max_count)

        return max_count