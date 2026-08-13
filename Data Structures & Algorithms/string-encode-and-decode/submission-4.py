class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        res = []
        for s in strs:
            res.append(str(len(s)))
            res.append(',')
        res.append('#')
        res.extend(strs)
        return "".join(res)


    def decode(self, s: str) -> List[str]:
        if len(s) == 0:
            return []

        sizes = []
        res = []
        i = 0
        while s[i] != '#':
            j = i
            while s[j] != ',':
                j += 1
            size = int(s[i:j])
            sizes.append(size)
            i = j + 1
        i += 1
        for size in sizes:
            word = s[i:i+size]
            i += size
            res.append(word)
        return res
            
