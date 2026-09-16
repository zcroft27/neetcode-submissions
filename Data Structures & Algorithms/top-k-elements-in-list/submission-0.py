class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        # idx is count, val is list of nums with that count
        bucket = [[] for _ in range(len(nums)+1)]

        for num in nums:
            count[num] = 1 + count.get(num, 0)

        for val, ct in count.items():
            bucket[ct].append(val)

        res = []
        idx = len(nums)
        while idx >= 0 and len(res) < k:
            if bucket[idx]:
                res += bucket[idx]
            idx -= 1

        return res[0:k]