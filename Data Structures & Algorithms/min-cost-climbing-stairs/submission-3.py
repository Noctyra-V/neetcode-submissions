class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [-1]*len(cost)
        def dfs(i,current_cost):
            if i >= len(cost):
                return 0
            if dp[i] != -1:
                return dp[i]
            dp[i] = cost[i] + min(dfs(i+1,cost[i] + current_cost),dfs(i+2,cost[i]+current_cost))
            return dp[i]
        n = dfs(0,0)
        p = dfs(1,0)
        return min(n,p)

# Solution made by looking at hints
