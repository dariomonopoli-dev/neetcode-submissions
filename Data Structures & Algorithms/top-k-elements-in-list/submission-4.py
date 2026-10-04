from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        res = []
        for num in nums:
            counts[num] +=1
        counts = dict(sorted(counts.items(), key=lambda item: item[1], reverse=True))
        keys = list(counts.keys())
        for i in range(k):
            res.append(keys[i])

        return res


        