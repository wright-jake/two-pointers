#example input
nums = [1,2,3,4,5,6,7], k = 3

#solution
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #to avoid dealing with bigger k values, we can mod k by the length of the list to work out how many rotations we 'actually' need
        k = k % len(nums)
        
        #initialise left and right pointers
        left, right = 0, len(nums) - 1
        
        #first of all we will reverse the entire list
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left = left + 1
            right = right - 1
         
        #then we will reverse the 'k' part/the part of the list we actually want to be rotated round
        left = 0
        right = k - 1
        
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left = left + 1
            right = right - 1
        
        #then we will reverse the other part of the list/the part we are not rotating    
        left = k
        right = len(nums) - 1
        
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left = left + 1
            right = right - 1
