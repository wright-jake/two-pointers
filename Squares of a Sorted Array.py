#example input
nums = [-4,-1,0,3,10]

#solution
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        #create two pointers
        left = 0
        right = n - 1
        
        #create blank array the same length as the original array
        result = [0] * n
        
        #we want to insert the biggest number at the end first, and then the next biggest etc
        for i in range(n - 1, -1, -1):
            
            #absolute value of function as easier to compare
            if abs(nums[left]) < abs(nums[right]):
                
                #we are taking the bigger number
                square = nums[right]
                
                #if we have used right pointer then create new one
                right -= 1
            else:
                #if absolute value of left number is bigger then that is the value we want to take
                square = nums[left]
                
                #used left pointer so create new one
                left += 1
             
            #result array will be filled from right to left/biggest to smallest
            result[i] = square * square
        return result
