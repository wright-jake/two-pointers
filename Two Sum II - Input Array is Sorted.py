#example input
numbers = [2,7,11,15], target = 9

#solution
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #use two pointer technique as list is sorted
        left = 0
        right = len(numbers)-1
        
        while left < right:
            sum = numbers[left] + numbers[right]
            if sum < target:
                left += 1
            elif sum > target:
                right -= 1
            else:
                return [left+1, right+1]
