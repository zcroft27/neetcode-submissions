class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # brute force:
        # for each element, iterate to the right, find max, replace with curr
        # instead, sliding window:
        # put whole list into a set, find max of them
        # left = max of those to the right, remove from set, increment left
        # OR:
        # iterate reverse: each element is the max seen
        max_seen = arr[len(arr)-1]
        for r in range(len(arr)-1, -1, -1):
            tmp = arr[r]
            arr[r] = max_seen
            max_seen = max(max_seen, tmp)
        arr[len(arr)-1] = -1
        return arr