class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        res = set()
        for num in nums:
            if num in counts:
                counts[num] +=1
            else:
                counts[num] = 1
        counts = dict(sorted(counts.items(), key=lambda item: item[1], reverse=True))
        for i in range(k):
            res.add(list(counts.keys())[i])

        return list(res)


        