#  9. Trapping Rain Water 
# Description: Given n non-negative integers representing elevation, compute how much water can be 
# trapped

# Input: 
height = [0,1,0,2,1,0,1,3,2,1,2,1] 
 
# Output: 
# 6


# Idea: calculate max in left and right and then waterlevel and finally trapped water

n = len(height)

lmax = [0] * n
lmax[0] = height[0]

for i in range(1,n):
    lmax[i] = max(lmax[i-1], height[i])


rmax = [0] * n
rmax[n-1] = height[n-1]
for i in range(n-2,-1,-1):
    rmax[i] = max(rmax[i+1], height[i])


waterlevel = [0] * n
trapped_water = 0

for i in range(n):
    waterlevel[i] = min(lmax[i], rmax[i])
    trapped_water += waterlevel[i] - height[i]


print(trapped_water)


