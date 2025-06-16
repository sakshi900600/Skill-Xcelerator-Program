#  Find Cricketers with Consistent Form (Avg > 60)

data = { 
  "Dhoni": [50, 60, 55], 
  "Kohli": [100, 90, 80], 
  "Hardik": [30, 40, 50] 
}

def findAvg(li):
    avg = 0
    sum = 0
    for i in range(len(li)):
        sum += li[i]
    avg = sum//len(li)
    return avg


for key,value in data.items():
    val = value
    avg = findAvg(val)

    if avg > 60:
        print(key)