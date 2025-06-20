#  Print the multiplication table of a number entered by the user.


num = int(input("Enter a number: "))


for i in range(1,11):
    print(f"{num} * {i} = {num*i}")


# output:
# Enter a number: 3
# 3 * 1 = 3
# 3 * 2 = 6
# 3 * 3 = 9
# 3 * 4 = 12
# 3 * 5 = 15
# 3 * 6 = 18
# 3 * 7 = 21
# 3 * 8 = 24
# 3 * 9 = 27
# 3 * 10 = 30