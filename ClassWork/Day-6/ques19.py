# Create a function that sums all even numbers from a list

li = [1,2,3,4,5,6]

def even_sum(li):
    sum = 0

    for item in li:
        if item%2 == 0:
            sum += item
    return sum


print(even_sum(li))
#output: 12