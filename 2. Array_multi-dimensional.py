import numpy as np

a_2d = np.array([[1, 2, 3], [4, 5, 6]]) #list inside list
print(a_2d)

#Summing every rows
def rowWiseSum(arr_2d):
    row,col= arr_2d.shape
    result_arr= np.zeros(row, dtype=int)
    for i in range(row):
        sum=0
        for j in range(col):
            sum+=arr_2d[i][j]
        result_arr[i]=sum
    return result_arr
a_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(rowWiseSum(a_2d))

#Summing every columns
def colWiseSum(arr_2d):
    row,col= arr_2d.shape
    result_arr=np.zeros(col, dtype=int)
    for j in range(col):
        sum=0
        for i in range(row):
            sum+=arr_2d[i][j]
        result_arr[j]=sum
    return result_arr
a_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(colWiseSum(a_2d))
print("-----------------------------")

#Swapping columns
def swapCols(arr_2d): #while swapping col-->row doesn't change
    row, col = arr_2d.shape
    for i in range(row):
        for j in range(col//2):
            temp= arr_2d[i][j]
            arr_2d[i][j]=arr_2d[i][col-1-j]
            arr_2d[i][col-1-j]=temp
    return arr_2d
a_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(a_2d)
print()
print("After swapping columns: ")
print(swapCols(a_2d))
print("-----------------------------")

#Swapping rows
def swapRows(arr_2d):
    row,col= arr_2d.shape
    for j in range(col):
        for i in range(row//2):
            temp=arr_2d[i][j]
            arr_2d[i][j]=arr_2d[row-1-i][j]
            arr_2d[row-1-i][j]=temp
    return arr_2d
a_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(a_2d)
print()
print("After swapping rows: ")
print(swapRows(a_2d))

