class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            stringS = ''.join(sorted(s))
            res[stringS].append(s)
        return list(res.values())






