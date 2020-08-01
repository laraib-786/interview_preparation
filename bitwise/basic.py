x=3
y=6
print(x & y)
print(x | y)
print(x ^ y)
print(x<<4)

def d_b(num,count):
    if num>1:
        d_b(num//2,count)
    #print(num%2)
    if num%2==1:
        count+=1
        print(count)
    return count
count=0
d_b(3,count)
def CountBits(n):
    total=0
    for i in range(1,n+1):
        count=0
        count=d_b(i,count)
        #print(count)
        total+=count
    return total
#print(CountBits(4))
