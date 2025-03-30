class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        n =len(temperatures)
        answer = [0]*n
        st = [0]
        for i in range(1,n):
            while st and temperatures[st[-1]] < temperatures[i] :
                answer[st[-1] ] =i-st[-1] 
                st.pop()
            st.append(i)
        return answer


