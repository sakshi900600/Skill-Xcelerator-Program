s = "1432219"
k = 3

# s = "10"
# k = 2

# s = "10200"
# k = 1



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