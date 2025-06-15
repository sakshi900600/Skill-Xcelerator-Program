# 3. 🧪 Scientific Term Extraction 
#  Task: Extract and print the word that comes after "is". 

# Input: text = "The mitochondria is the powerhouse  of the cell" 
#  Expected Output: "the"

s = "The mitochondria is the powerhouse is of the cell is"

s = s.split(" ")
# print(s)

for i in range(len(s)-1):
    if s[i] == "is":
        print(s[i+1])
    