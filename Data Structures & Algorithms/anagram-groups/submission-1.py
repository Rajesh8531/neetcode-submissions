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
        counts = [0 for _ in range(26)]
        value = 97
        for char in s:
            index = ord(char)-value
            if index > 26:
                return False
            counts[index] += 1
        for char in t:
            index = ord(char)-value
            if counts[index] == 0:
                return False
            counts[index] -= 1
        
        for count in counts:
            if count != 0:
                return False
        return True






