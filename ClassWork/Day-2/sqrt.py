n = 1225


si = 1
ei = n+1
ans = -1

while si < ei:
    mid = (si+ei)//2

    if mid * mid == n:
        ans = mid
        break
    elif mid*mid < n:
        ans = mid
        si = mid+1
    else:
        ei = mid-1


print(ans)