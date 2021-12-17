#example input
nums = [1,1,2]

#solution
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #initialise slow pointer
        slow = 0
        
        #fast pointer will compare slow pointer to the rest of the list
        for fast in range(1, len(nums)):
            
            #if not a duplicate then insert the value after the previous non-duplicate
            if nums[slow] != nums[fast]:
                nums[slow+1] = nums[fast]
                
                #keep slow pointer iterating through list
                slow += 1
        
        #we have been looking at index numbers so for our return value we want the number of non-duplicate elements
        return slow+1
