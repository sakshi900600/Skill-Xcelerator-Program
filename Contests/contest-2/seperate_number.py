#  ques is given a string and our task is to divide the string in such a way that every a[I]-a[i-1] = 1 and there should be no leading zero.


# logic: take first substr of different length but coz we need 1 difference b/n substr so first substr length can go upto n/2 and in case of odd n/2+1
# we will fix first str and check for next num by doing +1 in first str and if valid and possible then we will keep doing the same and at last return true or fasle acc.


# clarifiactions: 
# 1.  we loop len_first from 1 to n//2 +1:  coz must be at least one digit. if first_str uses more than n//2 digits then there will not left digits to make the next_str . doing +1 coz range fun stop 1 index before and we want to include the last one as well. 

# example: For "1234" (n=4), the first number’s max length is 2 (e.g., "12" → next number "34", but 34 != 12 + 1) and if we take "123" -> next no "124" which is not possible coz we are left with only 1 digit.




s = "1234" # true
# s = "99100" # true
# s = "010203" # false



def seperate_number(s):
    n = len(s)

    for len_first in range(1,n//2+1):
        first_str = s[:len_first]

        if len(first_str) > 1 and first_str[0] == '0':
            continue

        num = int(first_str)
        next_num = num + 1

        curr_pos = len_first
        valid = True

        while curr_pos < n: 
            next_str = str(next_num)
            if not s.startswith(next_str,curr_pos):
                valid = False
                break

            curr_pos += len(next_str)
            next_num += 1
        
        if valid and curr_pos==n:
            return f"YES {first_str}" 
        
    return "NO"


print(seperate_number(s))

    

