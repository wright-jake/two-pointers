#example input
nums = [0,1,0,3,12]

#solution
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #the idea is that if we find any non-zero elements, these will move to the previous index which changes based on each non-zero element found
        prev_idx = 0
        
        for i in range(0,len(nums)):
            if nums[i] != 0:
                nums[prev_idx], nums[i] = nums[i], nums[prev_idx]
                prev_idx += 1
