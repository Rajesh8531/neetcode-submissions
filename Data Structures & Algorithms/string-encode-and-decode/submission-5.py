class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        res = []
        for s in strs:
            res.append(str(len(s)))
            res.append('#')
            res.append(s)
        return ''.join(res)


    def decode(self, s: str) -> List[str]:
        if len(s) == 0:
            return []

        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            size = int(s[i:j])
            i = j + 1
            res.append(s[i:i+size])
            i += size
        return res
            
