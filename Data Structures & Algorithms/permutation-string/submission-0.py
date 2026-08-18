class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count1 = [0] * 26
        count2 = [0] * 26

        for ch in s1:
            index = ord(ch) - ord('a')
            count1[index] += 1

        l = 0
        for r in range(len(s2)):
            char = s2[r]
            index = ord(char) - ord('a')
            count2[index] += 1
            if self.hasSameChars(s1,count1,count2):
                while r - l + 1 > len(s1):
                    ch = s2[l]
                    index = ord(ch) - ord('a')
                    count2[index] -= 1
                    l += 1
            if r-l+1 == len(s1) and self.isAnagram(count1,count2):
                return True
        return False
        
    def isAnagram(self,count1,count2):
        for i in range(len(count1)):
            if count1[i] != count2[i]:
                return False
        return True

    def hasSameChars(self,s1,count1,count2):
        for ch in s1:
            index = ord(ch) - ord('a')
            if count2[index] < count1[index]:
                return False
        return True