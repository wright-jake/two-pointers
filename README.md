# two-pointers
A collection of all my data structure and algorithm solutions where the two pointers technique has been implemented 

Commonly used when trying to find pairs in an array/linked list that meet a certain condition or reversing an array/linked list

If looking at an array of numbers, we want to sort this and then create two pointers (left and right): 

    left = 0 
    right = (len(array)-1)
    
Perform the operation you are looking for:

    sum = array[left] + array[right]
    
If the value you got is less than your target increase the left pointer and vice versa:

    if sum < target:
      left += 1
    else:
      right -= 1

We can also have slow and fast pointers where the fast pointer increases at a faster rate i.e. increments by 2 each time while the slow pointer increments by 1 (see 'Middle of the Linked List' for an example

We can perform all of these on linked lists too, to increment with these we use .next (see 'Remove Nth Node from End of List' as an example)
