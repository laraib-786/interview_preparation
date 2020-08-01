def TOH(n,A,B,C):
    if n>0:
        TOH(n-1,A,C,B)
        print("Move a disc from {} to {}".format(A,C))
        TOH(n-1,B,A,C)
#TOH(8,1,2,3)
def multiplyMatrix(n1, m1, n2, m2, arr1, arr2):
    k=0
    mul_mat=[[0]*m2]*n1
    if n1==n2==m1==m2==1:
        print(arr1[0][0] * arr2[0][0])
    else:
        for i in range(0,n1):
            for j in range(0,m2):
                mul_mat[i][j] = arr1[i][k] * arr2[k][j] + arr1[i][k+1] * arr2[k+1][j]
                print(mul_mat[i][j],end=" ")
#multiplyMatrix(3,2,2,2,[[4,8],[0,2],[1,6]],[[5,2],[9,4]])
multiplyMatrix(1,1,1,1,[[2]],[[3]])
multiplyMatrix(1,5,5,2,[[1,2,3,4,5]],[[1,2],[1,2],[1,2],[1,2],[1,2]])
