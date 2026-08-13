class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapper = {}
        for string in strs:
            key = self.get_char_count(string)
            if key not in mapper:
                mapper[key] = []
            mapper[key].append(string)
        return [value for _, value in mapper.items()]



    def get_char_count(self,string):
        arr = [0] * 26
        for ch in string:
            index = ord(ch) - ord('a')
            arr[index] += 1
        return tuple(arr)

        