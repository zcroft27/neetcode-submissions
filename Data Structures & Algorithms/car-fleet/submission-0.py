class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        combo = sorted(zip(position, speed), reverse=True)
        stack = []
        for pos, speed in combo:
            curr_time = (target-pos)/speed
            if stack:
                front_time = stack[-1]
                if curr_time > front_time:
                    stack.append(curr_time)
            else:
                stack.append(curr_time)

        return len(stack)