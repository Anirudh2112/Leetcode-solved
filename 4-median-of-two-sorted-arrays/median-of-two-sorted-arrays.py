class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Ensure nums1 is the smaller array for efficiency
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        # Get lengths
        x, y = len(nums1), len(nums2)
        # Calculate total length and required positions
        total = x + y
        half = (total + 1) // 2  # Works for both odd and even lengths
        
        # Binary search boundaries
        low, high = 0, x
        
        while low <= high:
            # Partition the smaller array
            partitionX = (low + high) // 2
            # Calculate partition of larger array based on smaller array's partition
            partitionY = half - partitionX
            
            # Find elements around the partition
            maxX = float("-inf") if partitionX == 0 else nums1[partitionX - 1]
            minX = float("inf") if partitionX == x else nums1[partitionX]
            maxY = float("-inf") if partitionY == 0 else nums2[partitionY - 1]
            minY = float("inf") if partitionY == y else nums2[partitionY]
            
            # Check if we found the correct partition
            if maxX <= minY and maxY <= minX:
                # If total length is odd, median is max of left halves
                if total % 2 != 0:
                    return max(maxX, maxY)
                # If total length is even, median is average of max of left halves and min of right halves
                else:
                    return (max(maxX, maxY) + min(minX, minY)) / 2
            # Adjust binary search boundaries
            elif maxX > minY:
                high = partitionX - 1  # Move left in nums1
            else:
                low = partitionX + 1  # Move right in nums1
