# if IP address is valid then if it is IPV4 or IPV6 address print IPV4, IPV6 otherwise Neither .


# ip = "172.16.254.1" # IPv4
ip = "2001:0db8:85a3:0:0:8A2E:0370:7334"  # IPv6
# ip = "256.256.256.256" # Neither

def ipv4(str):
    str = str.split(".")
    # print(str)
    for i in range(len(str)):
        if len(str) != 4:
            return False
        
        if not str[i].isdigit():
            return False
        
        if not (0 <= int(str[i]) <=255):
            return False

        no = str[i]

        if len(no) > 1 and no[0] == '0':
            return False
    return True


def ipv6(str):
    str = str.split(":")
    # print(str)
    if len(str) != 8:
        return False
    
    valids = set("0123456789abcdefABCDEF")

    for num in str:
        if not (1 <= len(num) <= 4):
            return False
        
        for ch in num:
            if ch not in valids:
                return False
            
    return True

    



if ipv4(ip) == True:
    print("IPv4")
elif ipv6(ip) == True:
    print("IPv6")
else:
    print("Neither")
