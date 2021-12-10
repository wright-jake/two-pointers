#example input
s = ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]

#solution
class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        #create basic two pointers - left and right, to reverse entire array
        n = len(s)
        left = 0
        right = n - 1
        
        #will stop when entire array is reversed as either left = right or left > right
        while left < right:
            #swap letters on the outside first, then one letter in etc
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        
        #now create two more pointers, both starting from 0, one slow and one fast i.e. one iterates through the array faster than the other
        slow = 0
        fast = 0
        while fast < n:
            #searching for spaces to so then we can detect where a word starts and finishes
            while fast < n and s[fast] != " ":
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

        return s
