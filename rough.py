import numpy as np
t=int(input())
for i in range(t):
    row1=list(map(int, input().split()))
    row2=list(map(int, input().split()))
    matrix=np.array([row1,row2])
    mat=np.rot90(matrix, -1)
    if mat[0][0]>mat[0][1] or mat[0][0]>mat[1][0] or mat[1][0]>mat[1][1]:
        print("NO")
    else:
        print("YES")
