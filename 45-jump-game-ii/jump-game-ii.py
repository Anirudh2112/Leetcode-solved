class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0

        jumps = 0
        current_end = 0
        current_farthest = 0
        
        for i in range(n):
            current_farthest = max(current_farthest, i + nums[i])
            if i == current_end:
                jumps += 1
                current_end = current_farthest
                if current_end >= n - 1:
                    break
        
        return jumps