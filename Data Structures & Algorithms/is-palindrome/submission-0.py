class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = []
        for ch in s:
            if ch.isalnum():
                s1.append(ch.lower())
        string = "".join(s1)
        return string == string[::-1]