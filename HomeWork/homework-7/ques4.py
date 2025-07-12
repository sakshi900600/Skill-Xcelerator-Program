#  4. Remove All Adjacent Duplicates in String K 
# Description: Given a string and an integer k, remove k adjacent duplicate characters. 
# Input: 
s = "deeedbbcccbdaa" 
k = 3  # "aa"
 

# s = "abcd"
# k = 2  # "abcd"


# logic: I tried to store elem in stack. And did this
# 1. if stack is empty or curr elem doesn't match with top elem then put curr elem with 1 freq. 
# 2. if curr elem match with stack top elem then increase its frequency. 
# 3. if top elem freq == k then pop it from stack.
# 4. Build answer by doing freq*char 
# 5. return answer.


n = len(s)
st = []

for i in range(n):

    if len(st) == 0 or s[i] != st[-1][0]:
        st.append([s[i],1])
    
    elif st and s[i] == st[-1][0]:
        st[-1][1] = st[-1][1] + 1

    if st and st[-1][1] == k:
        st.pop()


# print(st)
ans = ""
while len(st) != 0:
    ch = st[-1][0]
    freq = st[-1][1]
    ans = (freq * ch) + ans
    st.pop()


print(ans)

