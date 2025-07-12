#  7. Sliding Window Maximum (Queue-based) 
# Description: Given an array and a window size k, print the max of each subarray of size k. 
# Input: 
nums = [1,3,-1,-3,5,3,6,7] 
k = 3 
 
# Output: 
# [3, 3, 5, 5, 6, 7] 


# My approach:  I will take a queue and i iwll always maintain exactly k elem in queue and get max of all k elem and store it in answer and after storing i will pop one elem from it. ultimately we get our answer.




class Queue:
    def __init__(self, queue_cap):
        self.capacity = queue_cap
        self.first = -1
        self.end = -1
        self.container = [0]*queue_cap
    
    
    def push(self,data):
        if self.end >= self.capacity-1:
            return
        
        if self.end == -1:
            self.end = 0
            self.first = 0
            self.container[self.end] = data
            return

        self.end += 1
        self.container[self.end] = data

    
    def pop(self):
        if self.first < 0:
            return
        
        data = self.container[self.first]

        if self.first == self.end:
            self.first = -1
            self.end = -1
        else:
            self.first += 1
        return data
        
    
    def peek(self):
        if self.is_empty():
            return
        
        return self.container[self.first]

    
    def is_empty(self):
        return self.first < 0
    
    def is_full(self):
        return self.end >= self.capacity-1
    
    def getmax(self):
        maxi = self.container[0]
        for i in range(len(self.container)):
            if self.container[i] > maxi:
                maxi = self.container[i]
        
        return maxi
    

n = len(nums)
q = Queue(1000)
li = [0] *n

j = 0
count = 0
for i in range(len(nums)):
    if count <= k:
        q.push(nums[i])
        count += 1

    li[j] = q.getmax()
    j += 1
    q.pop()
    count -= 1

print(li)






