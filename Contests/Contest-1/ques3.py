# # print the rangoli: You will be given an integer n and you need to print rangoli like this: 

# #size 3

# ----c----
# --c-b-c--
# c-b-a-b-c
# --c-b-c--
# ----c----

# #size 5

# --------e--------
# ------e-d-e------
# ----e-d-c-d-e----
# --e-d-c-b-c-d-e--
# e-d-c-b-a-b-c-d-e
# --e-d-c-b-c-d-e--
# ----e-d-c-d-e----
# ------e-d-e------
# --------e--------



n = 10

# first finding the char for specified size
alphabet = [chr(i) for i in range(97,123)]
alphabet = alphabet[:n]
# print(alphabet)


# now finding the indexes
ind = list(range(n)) 
# ind = ind[::-1] # it will give reversed index
# ind = ind[:-1] # it will give 1 less index,  coz last is excluded
ind = ind[:-1] + ind[::-1] 
# print(ind)



# now placing the alphabet on index

for i in ind:
    start_ind = i+1
    original = alphabet[-start_ind:]
    reverse = original[::-1]
    row = reverse + original[1:]
    row = "-".join(row)

    # now string is created with - in b/n char
    # to add spaces in its both side: center method is used

    width = n*4-3
    row = row.center(width, "-")
    print(row)