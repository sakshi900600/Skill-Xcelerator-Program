# Check for Anagram Players

# output: True
# player1 = "listen" 
# player2 = "silent" 


# output: False
player1 = "listen" 
player2 = "abc" 


def anagram(s1, s2):
    if len(s1) != len(s2):
        return False
    else:
        s1 = sorted(s1)
        s2 = sorted(s2)
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                return False
            
    return True


print(anagram(player1, player2))