class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        def dfs(i):
            if(len(employee[i]) == 0):
                return informTime[i]
            else:
                return max(dfs(j) for j in employee[i]) + informTime[i]
            
        employee = [[] for i in range(n)]
        for i in range(n):
            if(manager[i] >= 0):
                employee[manager[i]].append(i)
        return dfs(headID)