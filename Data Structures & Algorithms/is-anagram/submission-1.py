class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        firstMap = {}

        for char in s:
            firstMap[char] = firstMap.get(char, 0) + 1
        
        secondMap = {}

        for char in t:
            secondMap[char] = secondMap.get(char, 0) + 1
        
        return firstMap == secondMap