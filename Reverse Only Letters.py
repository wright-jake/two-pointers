#example input
s = "ab-cd"

#solution
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        
        #python strings are immutable so convert to a list
        s = list(s)
        
        #initialise pointers
        left, right = 0, len(s) - 1
        
        #iterate through array
        while left < right:
            
            #we set our pointers to only letters and increment past anything else
            while left < right and not s[left].isalpha():
                left += 1
            while left < right and not s[right].isalpha():
                right -= 1
            
            #reverse letters
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        
        #return letters from list all joined up
        return ''.join(s)
