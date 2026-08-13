class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapper = {}
        for string in strs:
            sorted_str = "".join(sorted(string))
            if sorted_str not in mapper:
                mapper[sorted_str] = []
            mapper[sorted_str].append(string)
        return [value for _, value in mapper.items()]
        