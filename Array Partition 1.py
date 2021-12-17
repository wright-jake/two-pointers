#example input
nums = [6,2,6,5,1,2]

#solution
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        
        #sort array
        nums.sort()
        
        #initialise sum variable
        sum = 0
        
        #initialise pointers
        left = 0
        right = 1
        
        #iterate pointers through list
        while right <= len(nums) - 1:
            
            #we want the minimum number from each pair added into our sum
            sum += min(nums[left],nums[right])
            
            #increment pointers to the next pair
            left += 2
            right += 2
        
        #return answer 
        return sum
