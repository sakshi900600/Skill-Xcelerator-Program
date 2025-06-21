# you can only take n/2 canday and your task is to maximize the types. 



def distribute_candy(candyType):
    allowed_candy = len(candyType)//2

    unique_candy = set(candyType)
    # print(unique_candy)

    if len(unique_candy) == allowed_candy:
        return allowed_candy
    elif len(unique_candy) > allowed_candy:
        return allowed_candy
    elif len(unique_candy) < allowed_candy:
        return len(unique_candy)



# candyType = [1,1,2,2,3,3]  #output: 3
# candyType = [1,1,2,3]  #output: 2
candyType = [6,6,6,6]  #output: 1

print(distribute_candy(candyType))



