class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            code = [0] * 26
            for ch in s:
                index = ord(ch) - ord('a')
                code[index] += 1
            res[tuple(code)].append(s)
        return list(res.values())






