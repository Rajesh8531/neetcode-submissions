class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts = [0 for _ in range(26)]
        value = 97
        for char in s:
            index = ord(char)-value
            if index > 26:
                return False
            counts[index] += 1
        for char in t:
            index = ord(char)-value
            if counts[index] == 0:
                return False
            counts[index] -= 1
        
        for count in counts:
            if count != 0:
                return False
        return True