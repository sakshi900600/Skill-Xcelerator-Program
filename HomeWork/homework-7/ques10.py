# 10. Asteroid Collision 
# Description: Simulate the collision of asteroids moving towards each other. 
# Input: 
# asteroids = [5, 10, -5] 
asteroids = [-2,-1,1,2]  # ans = [-2,-1,1,2]  

 
# Output: 
# [5, 10]


stack = []
n = len(asteroids)
for i in range(n):
    if asteroids[i] > 0:
        stack.append(asteroids[i])
    
    else:
        while stack and stack[-1] > 0 and abs(asteroids[i]) > stack[-1]:
            stack.pop()
        
        if not stack or stack[-1] < 0:
            stack.append(asteroids[i])
        elif stack[-1] == abs(asteroids[i]):
            stack.pop()


print(stack)