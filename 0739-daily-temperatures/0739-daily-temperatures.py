class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack =[0]
        n=  len(temperatures)
        ans = [0] * n
        for i in range(1,n):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                idx = stack.pop()
                ans[idx] = i - idx
            stack.append(i)
        return ans 