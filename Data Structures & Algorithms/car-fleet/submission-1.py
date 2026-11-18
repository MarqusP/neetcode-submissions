class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[p, s] for p, s in zip(position, speed)]
        pair = sorted(pair)
        stack = []

        for i in reversed(pair):
            if not stack:
                stack.append(i)
                continue
        
            time = (target - i[0]) / i[1]
            t_time = (target - stack[-1][0]) / stack[-1][1]

            if t_time < time:
                stack.append(i)

        return len(stack)