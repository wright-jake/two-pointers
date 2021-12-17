#example input
image = [[1,1,0],[1,0,1],[0,0,0]]

#solution
class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        #we want to deal with each row
        for row in image:
            
            #initialise pointers
            left, right = 0, len(row) - 1

            #iterate through row
            while left <= right:
                
                #how we deal with the middle of the row
                if left == right:
                    row[left] = abs(1 - row[left])

                else:
                    #invert the image
                    row[left] = abs(1 - row[left])
                    row[right] = abs(1 - row[right])
                    
                    #flip the image
                    row[left], row[right] = row[right], row[left]

                #increment pointers
                left += 1
                right -= 1
        
        #return flipped image
        return image
