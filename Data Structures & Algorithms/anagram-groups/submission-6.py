class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        words = {}
        for word in strs:
            count = [0] * 26
            for letter in word:
                count[ord(letter) - ord('a')] += 1

            key = tuple(count)

            if key not in words:
                words[key] = []
            words[key].append(word)

        return list(words.values())
 
