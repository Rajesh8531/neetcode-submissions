class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        countArr = [0] * 26
        for ch in s:
            index = ord(ch) - ord('a')
            countArr[index] += 1

        for ch in t:
            index = ord(ch) - ord('a')
            if countArr[index] == 0:
                return False
            countArr[index] -= 1

        return True
        