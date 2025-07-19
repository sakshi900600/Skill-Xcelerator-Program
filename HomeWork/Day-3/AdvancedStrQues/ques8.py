# Find the smallest substring that contains all characters of a given target string.  
# Input: s = "ADOBECODEBANC", t = "ABC" → Output: "BANC"


s = "ADOBECODEBANC"
t = "ABC"

# s = "a"
# t = "aa"


# solution: 
        
# steps: first store the freq of char in t string
# use sliding window and everytime store the current char freq 
# in curr_freq dct and if freq of curr char is same as in req_freq then use a counter var and do count++
# if count == len(required) then while this is valid store the minlen and start_index(to get substr). 
# decrease freq of char at ith index  if s[i] is in required and its freq in curr_freq become less as in required then do count--
# if minlen not inf then return substrin from start_index to si + minlen else empty string


def minWindow(s, t):

        req_freq = {}

        for i in range(len(t)):
            req_freq[t[i]] = req_freq.get(t[i],0)+1

        

        curr_freq = {}
        i = 0
        count = 0
        minlen = float('inf')
        start_index = -1

        for j in range(len(s)):
            ch = s[j]
            curr_freq[ch] = curr_freq.get(ch,0)+1

            if curr_freq.get(ch) == req_freq.get(ch):
                count += 1
            
            if count == len(req_freq):
                while count == len(req_freq):
                    if j-i+1 < minlen:
                        minlen = j-i+1
                        start_index = i
                    
                    # shrink
                    curr_freq[s[i]] -= 1

                    if s[i] in req_freq and curr_freq[s[i]] < req_freq[s[i]]:
                        count -= 1
                    
                    i += 1
        
        if minlen != float('inf'):
            return s[start_index: start_index+ minlen]
        else:
            return ""

        

print(minWindow(s,t))


