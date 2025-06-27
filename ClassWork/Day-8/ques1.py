# # return nth prime number:
# # ex - n=3 ans = 5.


# # first store 100 prime no in a list then traverse through the given input array and return prime[ind-1] as nth prime number.



# sieve of 
prime = [True] * 100
prime[0], prime[1] = False, False


for i in range(len(prime)):
    if prime[i] == True:
        k = 2*i
        while k<100:
            prime[k] = False
            k = k+i



