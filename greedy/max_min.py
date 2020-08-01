#hO(nlogn)
def maxMin1(n, k, arr):
    arr.sort()#O(nlogn)
    max_min=arr[k-1]-arr[0]
    for i in range(0,n-k+1):#O(n-k)
        max1=arr[k-1+i]
        min1=arr[i]
        max_min=min(max1-min1,max_min)#focus
    return max_min

def maxMin2(n, k, arr):
    arr.sort()
    max_min=arr[k-1]-arr[0]
    max_min1=0
    for i in range(0,n-k+1):
        max_min1=arr[k-1+i]-arr[i]
        if max_min1<max_min:
            max_min=max_min1
    return max_min


def maxMin3(n, k, arr):
    arr.sort()
    return min((arr[k-1+i]-arr[i]) for i in range(0,n-k+1))
