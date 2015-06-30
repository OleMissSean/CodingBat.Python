"""Python List 1 exercise 2.

http://codingbat.com/prob/p179078

Given an array of ints, return True if the array is length 1 or more, and the first element and the last element are equal.

same_first_last([1, 2, 3]) → False same_first_last([1, 2, 3, 1]) → True same_first_last([1, 2, 1]) → True"""

def same_first_last(nums):
  
    if(len(nums) >= 1):
        x = nums[0]
        z = nums[-1]
        if(x == z):
           return True
        else:
           return False
    else:
        return False
