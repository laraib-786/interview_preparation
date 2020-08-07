#You have an infinite supply of coins, each having some value.
#Find out the number of ways to use the coins to sum-up to a certain required value.
#for coins=[2,5,3,6] ,no of ways=(2,2,2,2,2),(5,5),(3,3,2,2),(2,3,5),(2,2,4)
# Note: you can use coins with any no of times.

# method 1: Memoization
def nofways(coins,n,sum,memo):
    if n==0:
        return 0
    if sum==0:
        return 1
    if memo[n][sum]!=-1:
        return memo[n][sum]
    memo[n][sum]=nofways(coins,n-1,sum,memo)
    if coins[n-1]<=sum:
        memo[n][sum]=memo[n][sum]+nofways(coins,n,sum-coins[n-1],memo)
    return memo[n][sum]

def numberOfWays(coins,n,sum):
    memo=[[-1]*(sum+1) for i in range(0,n+1)]
    return nofways(coins,n,sum,memo)
print(numberOfWays([2,5,3,6],4,10))



# method 2: Tabulation
def numberOfWays1(coins,n,sum):
    tab=[[-1]*(sum+1) for i in range(0,n+1)]
    for i in range(0,sum+1): tab[0][i]=0
    for j in range(1,n+1): tab[j][0]=1
    for i in range(1,n+1):
        for j in range(1,sum+1):
            tab[i][j]=tab[i-1][j]
            if coins[i-1]<=j:
                tab[i][j]=tab[i][j]+tab[i][j-coins[i-1]]
    return tab[n][sum]
print(numberOfWays1([2,5,3,6],4,10))
