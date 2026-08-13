class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0
        if len(s) == 0:
            return maxLength
        
        seen = set()
        start = 0
        end = 0
        while end < len(s):
            if s[end] in seen:
                while s[start] != s[end]:
                    seen.remove(s[start])
                    start  += 1
                seen.remove(s[start])
                start += 1
            seen.add(s[end])
            maxLength = max(maxLength,len(seen))
            end += 1
        return maxLength

        