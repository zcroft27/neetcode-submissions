class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        count_of_gaps = {0: 0} # gap_from_left : freq
        for row in wall:
            curr = 0
            for i in range(len(row) - 1):
                brick = row[i]
                curr += brick
                count_of_gaps[curr] = count_of_gaps.get(curr, 0) + 1
        
        max_gap_freq = max(count_of_gaps.values())

        return len(wall) - max_gap_freq