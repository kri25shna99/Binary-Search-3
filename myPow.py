#Time complexity : O(nlogk) where n is the total number of nodes and logk each time adding k linkedlist in the heap
#Did this code successfully run on Leetcode : Yes
#youtube : https://youtu.be/rWaQTam6Z7c
class Solution:
    def myPow(self, x: float, n: int) -> float:
        #base condition
        if n==0:
            return 1.0
        #logic
        #dividing n/2 always 
        result = self.myPow(x,int(n/2))
        #if n is even 
        if n%2 ==0:
            return result*result
        #if n is odd then we need to multipy with the number
        else:
            #checking if number is negative or positive if it is negative then we will multiply by 1/x or positive then number itself
            if n<0:
                return result*result*1/x
            else:
                return result*result*x
