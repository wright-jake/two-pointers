#example input
nums = [1,1,0,1,1,1]

#solution
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        #initialise slow and fast pointers
        slow = 0
        fast = 0
        
        #initialise count
        count = 0
        
        while fast < len(nums):
            
            #if we encounter a zero move on
            while fast < len(nums) and nums[fast] == 0:
                fast += 1
            
            #when we first encounter a one, take the starting point
            slow = fast
            
            #when we encounter a one, we want to keep increasing the fast pointer until we come across a zero
            while fast < len(nums) and nums[fast] == 1:
                fast += 1
            
            #compare our count of ones, with the new count
            count = max(count, fast - slow)
        
        #return maximum count
        return count
