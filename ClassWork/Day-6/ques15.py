# Create a function print_ingredients() that prints three ingredients.

def print_ingredients(li):
    for i in range(len(li)):
        if i==3:
            break
        else:
            print(li[i])



li = ["Salt","Oil","Onion","Mango"]
print_ingredients(li)

# output:
# Salt
# Oil
# Onion