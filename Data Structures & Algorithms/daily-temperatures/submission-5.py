class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        output = [0] * len(temperatures)

        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                curr_temp = stack.pop()
                if temperatures[curr_temp] < temperatures[i]:
                    output[curr_temp] = i - curr_temp
                else:
                    stack.append(curr_temp)
            stack.append(i)
        return output