class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countChars = [0] * 26
        for char in s:
            index = ord(char) - ord('a')
            countChars[index] += 1
        
        for char in t:
            index = ord(char) - ord('a')
            if countChars[index] == 0:
                return False
            countChars[index] -= 1
        
        for count in countChars:
            if count != 0:
                return False
        return True