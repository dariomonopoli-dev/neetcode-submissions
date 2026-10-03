from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            l = [0] * 26
            for char in s:
                l[ord(char) - ord('a')] += 1
            tup = tuple(l)
            res[tup].append(s)
        return list(res.values())
