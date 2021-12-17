#example input
nums = [3,2,2,3], val = 3

#solution
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        #initialise pointers
        left = 0
        right = len(nums) - 1 
        
        #initialise count
        count = len(nums)
        
        #iterate pointers through loop
        while left <= right:
            
            #we want to leave the target values on the right side
            if nums[right] == val:
                right -= 1
                count -= 1
            
            #if right value is not equal to target value
            else:
                if nums[left] == val:
                    
                    #we want to change the left target value to the right non-target value
                    nums[left] = nums[right]
                    right -= 1
                    left += 1
                    count -= 1
                
                #if neither left or right values are equal to target then increment left pointer by 1
                else:
                    left += 1
        return count
