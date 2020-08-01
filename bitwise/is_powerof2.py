def is_powerof2(n):#O(n)
    if n>2:
        return True and is_powerof2(n/2)
    if n==2:
        return True
    else:
        return False
print(is_powerof2(1))



def ispower2(n):#O(1)
    if (n&(n-1))==0:
        print("Yes")
    else:
        print("No")
ispower2(1)


def ispower_2(n):
    if n==0:
        return False
    return n&(n-1)==0

print(ispower_2(1024))
