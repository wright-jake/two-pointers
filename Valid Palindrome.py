#example input
s = "A man, a plan, a canal: Panama"

#solution
class Solution:
    def isPalindrome(self, s: str) -> bool:
        #initialise pointers
        left, right = 0, len(s) - 1
        
        #iterate through the string
        while left < right:
            
            #if non-alphanumeric character increment the pointers
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            
            #if it is alphanumeric character and it isn't equal to the equivalent charcater then must not be palindrome
            if s[left].lower() != s[right].lower():
                return False
            
            #increment pointers
            left += 1
            right -= 1
        return True
