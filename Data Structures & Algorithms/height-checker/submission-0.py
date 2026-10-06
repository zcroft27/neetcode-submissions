class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        counts = [0] * 101

        for height in heights:
            counts[height] += 1
        
        expected = []
        for height, count in enumerate(counts):
            while count > 0:
                expected.append(height)
                count -= 1

        count_of_diffs = 0
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                count_of_diffs += 1

        return count_of_diffs