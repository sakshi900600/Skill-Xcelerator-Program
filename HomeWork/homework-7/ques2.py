# 2. Remove K Digits 
# Description: Given a number as a string and an integer k, remove k digits to make the smallest 
# possible number


# s = "1432219"
k = 3  # ans = 1219

# s = "10"
# k = 2  # ans = 0

s = "10200"
k = 1  # ans = 200


# logic:  store only the smaller elem in stack.  Every time compare top elem with current s[i] and until top elem is greater pop it from stack and decrease k . At last also check if k still not 0 then return only 0 to n-k elem as answer and here need to trim all leading 0 so do that as well. 


def removeKdigits(num, k):
        stack = list()

        for i in range(len(num)):
            while stack and int(stack[-1]) > int(num[i]) and k > 0:
                stack.pop()
                k -= 1
            
            stack.append(num[i])


        ans = stack
        if k > 0:
            ans = stack[0:len(stack)-k]

        final_str = "".join(ans)

        # print(final_str)
        if final_str == "" or int(final_str) == 0:
            return '0'
        else:
            return final_str.lstrip('0')


print(removeKdigits(s,k))