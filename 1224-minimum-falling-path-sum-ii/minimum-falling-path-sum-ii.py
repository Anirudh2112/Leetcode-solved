class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if n == 1:
            return min(grid[0])

        prev_dp = grid[0][:]

        for i in range(1, n):
            curr_dp = [0] * n
        
            min1_idx = -1
            min2_idx = -1
            
            for j in range(n):
                if min1_idx == -1 or prev_dp[j] < prev_dp[min1_idx]:
                    min2_idx = min1_idx
                    min1_idx = j
                elif min2_idx == -1 or prev_dp[j] < prev_dp[min2_idx]:
                    min2_idx = j

            for j in range(n):
                if j == min1_idx:
                    curr_dp[j] = prev_dp[min2_idx] + grid[i][j]
                else:
                    curr_dp[j] = prev_dp[min1_idx] + grid[i][j]
            
            prev_dp = curr_dp
        return min(prev_dp)

            