class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(str(len(s)))
            res.append('#')
            res.append(s)
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            size = int(s[i:j])
            i = j + 1
            string = s[i:i+size]
            res.append(string)
            i += size
        return res


