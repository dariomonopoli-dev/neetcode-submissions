class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts_s = {}
        counts_t = {}
        if len(s) != len(t):
            return False
        for char in s:
            if char in counts_s:
                counts_s[char] +=1
            else:
                counts_s[char] = 1

        for char in t:
            if char in counts_t:
                counts_t[char] +=1
            else:
                counts_t[char] = 1
        print(counts_s)
        print(counts_t)
        return (counts_s == counts_t)



        