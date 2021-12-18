#example input
s = "Let's take LeetCode contest"

#solution
class Solution:
    def reverseWords(self, s: str) -> str:
        
        #if string only has one letter then the reversed version will be the same as the original string
        if len(s) == 1:
            return s
        
        #python strings are immutable so convert to a list
        s = list(s)
        
        #create two pointers, both starting from 0, one slow and one fast i.e. one iterates through the array faster than the other
        slow, fast = 0, 0
        
        #iterate through array
        while fast < len(s):
            
            #searching for spaces to so then we can detect where a word starts and finishes
            while fast < len(s) and s[fast] != " ":
                
                #if it doesn't find space then move 1 to the right and check there etc
                fast += 1
            
            #takes the position of where the word is, we take one away from fast as currently it will be on the " " position
            left, right = slow, fast - 1
            
            #reverses the word
            while left < right:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
            
            #slow will now take position of starting letter of next word and loop will reiterate
            fast += 1
            slow = fast

        #return the letters from the list joined up
        return "".join(s)
