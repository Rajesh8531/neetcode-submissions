class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        frequency = 0
        length = 0
        l = 0
        count_map = {}
        for r in range(len(s)):
            ch = s[r]
            count_map[ch] = 1 + count_map.get(ch,0)
            frequency = max(frequency,count_map[ch])
            while r - l + 1 - frequency > k:
                count_map[s[l]] -= 1
                l += 1
            length = max(length,r-l+1)
        return length
                
        