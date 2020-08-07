def LIS(a,i,n):
    if i>=n-1:
        return i+1
    if a[i]<a[i+1]:
        return LIS(a,i+1,n)
    else:
        return max(LIS(a[0:i]+a[i+1:],0,n-1),LIS(a[0:i+1]+a[i+2:],0,n-1))

def longestSubsequence(a,n):
    return LIS(a,0,n)

def LIS(a,i,n,memo):
    if i>=n-1:
        return i+1
    if n==1:
        return 1
    if memo[i][n]!=-1:
        return memo[i][n]
    if a[i]<a[i+1]:
        memo[i][n]=LIS(a,i+1,n,memo)
    else:
        memo[i][n]=max(LIS(a[0:i]+a[i+1:],0,n-1,memo),LIS(a[0:i+1]+a[i+2:],i,n-1,memo))
    return memo[i][n]
def longestSubsequence(a,n):
    memo=[[-1]*(n+1) for i in range(0,n+1)]
    return LIS(a,0,n,memo)
def longestSubsequence1(arr , n ):

    # to allow the access of global variable
    global maximum
    if n == 1 :
        return 1
    maxEndingHere = 1
    for i in range(1, n):
        res = longestSubsequence1(arr , i)
        if arr[i-1] < arr[n-1] and res+1 > maxEndingHere:
            maxEndingHere = res +1
    maximum = max(maximum , maxEndingHere)

    return maxEndingHere
def longestSubsequence(arr,n):
    global maximum
    maximum = 1
    longestSubsequence1(arr , n)
    return maximum
