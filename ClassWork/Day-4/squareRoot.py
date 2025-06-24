# n = 8416  # ans = 91
n = 121  # 11

si = 0
ei = 100

ans = 0
while si <= ei:
    mid = (si+ei)//2
    square = mid * mid
    if(square == n):
        ans = mid
        break
    elif(square < n):
        ans = mid # it is being taken so that we can return the nearest value for non perfect square no.
        si = mid+1
    else:
        ei = mid-1

print(ans)


