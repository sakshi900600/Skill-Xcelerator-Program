# Get Top 2 Cricketers by Total Runs

stats = { 
  "Kohli": [60, 70, 100], 
  "Gill": [80, 90, 85], 
  "Rohit": [30, 40, 50] 
}

def findTotal(li):
    sum = 0
    for i in range(len(li)):
        sum += li[i]
    return sum


for name,run in stats.items():
    currtotal = findTotal(run)
    stats[name] = currtotal    


stats = sorted(stats)
print(stats[0])
print(stats[1])

    