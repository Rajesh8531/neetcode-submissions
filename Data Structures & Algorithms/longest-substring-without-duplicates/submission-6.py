class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        index_map = {}
        length = 0
        l = 0
        for r in range(len(s)):
            ch = s[r]
            if ch in index_map:
                l = max(l,index_map[s[r]] + 1)
            length = max(length,r-l+1)
            index_map[ch] = r
        return length
