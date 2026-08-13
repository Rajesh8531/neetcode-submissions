class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countMap = {}
        for char in s:
            if char not in countMap:
                countMap[char] = 0
            countMap[char] += 1
        
        for char in t:
            if char not in countMap:
                return False
            countMap[char] -= 1
        
        for _, value in countMap.items():
            if value != 0:
                return False
        return True