def getMinimumCost1(n, k, c):
    j=0
    i=0
    min_price=0
    c.sort()
    while(n-i)>0:
        for r in range(0,k):#add k prices every time
            if (n-i)>0:#Actually i iterates for n when i=n it iterates over all elements no ites are left >>so n>i means item left>>so include it
                i+=1
                min_price+=(j+1)*c[n-i] # n-i because start from last element
            else:
                break# in
        j+=1 # j will increase after every purchase of k flowers
    return min_price

def getMinimumCost2(n, k, c):#removal of j
    min_price=0
    c.sort()
    i=0
    while(k*(i)+1<=n):
            for j in range(k*i,k*(i+1)):#index (0,3),(3,6)
                try:
                    if (n-1-j)>=0:# if j=5, (n-1-j)=-1 =>c[-1] is included again so better to avoid it with if.
                        min_price+=(i+1)*c[n-1-j]
                except:return min_price# to avoid index error.
            i+=1
    return min_price
print(getMinimumCost2(5,3,[1,3,5,7,9]))


def getMinimumCost3(n, k, c):#most simplest
    min_price=0
    c.sort(reverse=True)#decending order
    i=0
    while(k*(i)+1<=n):
            for j in range(k*i,k*(i+1)):
                try:min_price+=(i+1)*c[j]
                except:return min_price
            i+=1
    return min_price
print(getMinimumCost1(5,3,[1,3,5,7,9]))

"""time complexity--O(n)[while loop-O(n/k) and for loop-(k)]"""
