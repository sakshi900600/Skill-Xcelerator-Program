# 3. Stock Span Problem 
# Description: For each day, calculate the number of consecutive days before it (including itself) the 
# stock price was less than or equal. 
# Input: 
# prices = [100, 80, 60, 70, 60, 75, 85] 
prices = [10, 4, 5, 90, 120, 80] 
n = len(prices)

# Output: 
# [1, 1, 1, 2, 1, 4, 6]

# ans = [0]*n

# 2 loops approach ------------------

# for i in range(n):
#     curr_elem = prices[i]
#     count = 0
#     for j in range(i,-1,-1):
#         if prices[j] <= curr_elem:
#             count += 1
#         else:
#             break
    
#     ans[i] += count

# print(ans)




# using stack logic -------------------
# first i try to store elem in stack but that doesn't work. So
# I stored index instead of value. popping out while top <= curr and calculating count by subtracting (curr idx - top idx). and if stack gets empty then storing (curr idx + 1) in ans list. 


ans = [1]*n

stack = []
stack.append(0)

for i in range(1,n):
    curr_elem = prices[i]
    while stack and prices[stack[-1]] <= curr_elem:
        stack.pop()
    
    if len(stack) == 0:
        ans[i] = i+1
    else:
        ans[i] = i-stack[-1]
    
    stack.append(i)


print(ans)
