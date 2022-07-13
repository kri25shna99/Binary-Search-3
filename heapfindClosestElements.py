#Time complexity : O(nlogk) where n is the total numbers logk each time adding k size in the heap
#Space complexity : O(k) where k is size of heap
#Did this code successfully run on Leetcode : Yes
#youtube : https://youtu.be/rWaQTam6Z7c
import heapq as hp
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        #defining max heap
        heap = []
        #iterating over elements of array
        for num in arr:
            #pushing the distance and the num as key key value pair in heap by making the number and magnitute negative
            hp.heappush(heap, (-1*abs(x-num),-1*num))
            #checking if the heap size increases than k after puching the element than we will pop the largest number value
            if len(heap)>k:
                hp.heappop(heap)
        #creating the result list for putting the k elements 
        result =[]
        #iterating over the elements in heap
        for i in heap:
            #fetching back the values 
            result.append(-1*i[1])
        #sort the result
        result.sort()
        return result
