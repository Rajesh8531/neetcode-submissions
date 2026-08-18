class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        length = 0
        mapper = {}
        for r in range(len(s)):
            if s[r] in mapper:
                l = max(mapper[s[r]]+1,l)
            mapper[s[r]] = r
            length = max(length,r-l+1)
        return length