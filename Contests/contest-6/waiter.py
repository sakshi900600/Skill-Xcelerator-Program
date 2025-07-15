# https://www.hackerrank.com/contests/cpu-skill-xcelerator-contest-6/challenges/waiter


# step 1: store prime no in a list to get ithprime
# step 2: loop from 1 to q+1 iteration
# every time if top elem is divisible by ithprime then put it in a list B and not then in another list A. 
# after one iteration put divisible list B into the ans list and also update the stack with the non-divisible stack/list A. 
# at last store the ramaining elem of list A into ans 
# return ans


# constraints: 
# Max value of number is 10000, and q can be 1200.
# The 1200th prime is 9733. So we need a sieve up to at least 9733. for safety and also number is 10000 so i take 10001.



def getithprime(val):
    prime = [True] * 10001 
    prime[0] = prime[1] = False

    for i in range(len(prime)):
        if prime[i] == True:
            k = 2 * i

            while k < 10001:
                prime[k] = False
                k = k + i
    

    count = 0
    ans = -1

    for i in range(len(prime)):
        if prime[i] == True:
            count += 1
            ans = i
        
        if count == val:
            break
    
    return ans



# number = [2,3,4,5,6,7]
number = [3,4,7,6,5]
q = 1

ans = []

for i in range(1,q+1):
    iprime = getithprime(i)
    A = [] # not divisible 
    B = [] # divisible

    while len(number) > 0:
        top = number.pop()
        if top % iprime == 0:
            B.append(top)
        else:
            A.append(top)
    
    while len(B) != 0:
        ans.append(B.pop())
    
    number = A.copy()


while len(A) != 0:
    ans.append(A.pop())


# print(ans)

# print(getithprime(1200))
