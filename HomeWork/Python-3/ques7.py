# Even-Length Words 
#  Task: Print only the words with even number of letters.  

# Input: sentence = "Science needs logic and curiosity" 


# s = "Science needs logic and curiosity" # ""

s = "I got placed in Google"

s = s.split(" ")
print(s)

for i in range(len(s)):
    if len(s[i]) % 2 == 0:
        print(s[i])