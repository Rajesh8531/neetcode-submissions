class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = []
        for ch in s:
            if ch.isalnum():
                s1.append(ch.lower())
        i = 0
        j = len(s1) - 1
        while i < j:
            if s1[i] != s1[j]:
                return False
            i += 1
            j -= 1
        return True