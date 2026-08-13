class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        solutions = []
        searchedIndex = set()
        length = len(strs)
        for i in range(length):
            if i in searchedIndex:
                continue
            ans = []
            firstString = strs[i]
            for j in range(i+1,length):
                secondString = strs[j]
                isValidAnagram = self.isAnagram(firstString,secondString)
                if isValidAnagram:
                    searchedIndex.add(j)
                    ans.append(secondString)
            ans.append(firstString)
            solutions.append(ans)
        return solutions
    
    def isAnagram(self,s,t):
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)