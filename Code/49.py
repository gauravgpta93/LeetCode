class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = dict()
        for word in strs:
            count = [0] * 26
            for l in word:
                count[ord(l) - ord("a")] += 1
            count = tuple(count)
            if count not in ans:
                ans[count] = [word]
            else:
                ans[count].append(word)
        return ans.values()
