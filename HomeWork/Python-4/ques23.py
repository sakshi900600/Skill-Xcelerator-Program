# List Cricketers Who Improved Over Matches

data = { 
  "Kohli": [30, 60, 90], 
  "Gill": [100, 80, 60] 
} 
 
# Output: Improving: ['Kohli']

def issorted(li):
    for i in range(len(li)-1):
        if li[i+1] < li[i]:
            return False
    return True


for name,runs in data.items():
    li = runs
    if issorted(li):
        print(name)