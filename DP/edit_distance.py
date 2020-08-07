# 1.wrong  not work for s1=sitting ,s2=kitten
def edit_distance(s1,s2,m,n):
    if m==n==0:
        return 0
    if s1[0]==s2[0]:
        return edit_distance(s1[1:],s2[1:],m-1,n-1)
    elif m>n:
        return 1+edit_distance(s1[1:],s2,m-1,n)
    elif m<n:
        #s1=s2[0]+s1
        #m+=1
        return 1+edit_distance(s1,s2[1:],m,n-1)
    else:
        # s1[o],s2[0]=s2[0],s1[0]
        return 1+edit_distance(s1[1:],s2[1:],m-1,n-1)

print(edit_distance("SATURDAY","SUNDAYON",8,8))
#Method1: Recursion
def edit_distance1(s1,s2,m,n,memo):
    if m==0:
        return n
    if n==0:
        return m
    if s1[m-1]==s2[n-1]:
        return edit_distance1(s1,s2,m-1,n-1,memo)
    else:
        return 1+min(edit_distance1(s1,s2,m-1,n,memo),edit_distance1(s1,s2,m-1,n-1,memo),edit_distance1(s1,s2,m,n-1,memo))





# Method2:Memoization
def edit_distance1(s1,s2,m,n,memo):
    if m==0:
        return n
    if n==0:
        return m
    if memo[m][n]!=-1:
        return memo[m][n]
    if s1[m-1]==s2[n-1]:
        memo[m][n]=edit_distance1(s1,s2,m-1,n-1,memo)
    else:
        memo[m][n]=1+min(edit_distance1(s1,s2,m-1,n,memo),edit_distance1(s1,s2,m-1,n-1,memo),edit_distance1(s1,s2,m,n-1,memo))
    return memo[m][n]
def edit_distance(s1,s2,m,n):
    memo=[[-1]*(n+1) for i in range(0,m+1)]
    return edit_distance1(s1,s2,m,n,memo)

#Method3:Tabulation
def edit_distance(s1,s2,m,n):
    tab=[[-1]*(n+1) for i in range(0,m+1)]
    for i in range(0,m+1):tab[i][0]=i
    for i in range(0,n+1):tab[0][i]=i
    for i in range(1,m+1):
        for j in range(1,n+1):
            if s1[i-1]==s2[j-1]:
                tab[i][j]=tab[i-1][j-1]
            else:
                tab[i][j]=1+min(tab[i-1][j],tab[i-1][j-1],tab[i][j-1])
    return tab[m][n]
