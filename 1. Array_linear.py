import numpy as np
class Array:

    @staticmethod
    def iterate(arr):
        for i in arr:
            print(i, end=" ")
        print()
    
    @staticmethod
    def resize(arr, newSize):
        resized= np.zeros(newSize, dtype=int)
        for i in range(min(len(arr),newSize)):
            resized[i] = arr[i]
        return resized
    
    @staticmethod
    def copy(arr):
        copied= np.zeros(len(arr), dtype=int)
        for i in range(len(copied)):
            copied[i]= arr[i]
        return copied
    
    @staticmethod
    def left_shift(arr):                    #2 3 4 5-->3 3 4 5-->3 4 4 5
        for i in range(len(arr)-1):         #3 4 5 5
            arr[i]=arr[i+1]
        arr[len(arr)-1]=0                   #-->3 4 5 0

    @staticmethod
    def right_shift(arr):
        for i in range(len(arr)-1,0,-1):    #2 3 4-->2 3 3-->2 2 3
            arr[i]=arr[i-1]
        arr[0]=0                            #-->0 2 3

    @staticmethod
    def left_rotate(arr):
        if len(arr)==0:
            return
        temp= arr[0]
        for i in range(len(arr)-1):
            arr[i]=arr[i+1]
        arr[len(arr)-1]=temp

    @staticmethod
    def reverse_out_of_place(arr):
        reversed_arr= np.zeros(len(arr), dtype= int)
        for i in range(len(arr)):
            reversed_arr[i]= arr[len(arr)-1-i]
        return reversed_arr
    
    @staticmethod
    def reverse_in_place(arr):
        left, right= 0, len(arr)-1
        while left< right:
            arr[left],arr[right]= arr[right],arr[left]
            left+=1
            right-=1

    @staticmethod
    def delete(arr, index, current_size):
        if index<0 or index >=current_size:
            raise IndexError("Invalid Index")
        for i in range(index,current_size-1):
            arr[i]=arr[i+1]
        arr[current_size-1]=0

"""Tester Code"""
if __name__=="__main__":
    array= np.array([1,2,3,4,5,0,0], dtype=int)
    current_size = 5

    print("Original array: ", end="")
    Array.iterate(array)

    print("Resized array: ", end="")
    resized = Array.resize(array, 10)
    Array.iterate(resized)

    print("Copied array: ", end="")
    copied = Array.copy(array)
    Array.iterate(copied)   

    print("Shift left: ", end="")
    Array.left_shift(array)
    Array.iterate(array)

    print("Shift right: ", end="")
    Array.right_shift(array)
    Array.iterate(array)

    print("Rotate left: ", end="")
    Array.left_rotate(array)
    Array.iterate(array)

    # print("Rotate right: ", end="")
    # Array.rotate_right(array)
    # Array.iterate(array)

    print("Reversed out-of-place: ", end="")
    reversed_out = Array.reverse_out_of_place(array)
    Array.iterate(reversed_out)

    print("Reversed in-place: ", end="")
    Array.reverse_in_place(array)
    Array.iterate(array)

    # print("After insertion: ", end="")
    # array = Array.insert(array, 2, 10, current_size)
    # current_size += 1
    # Array.iterate(array)

    array= np.array([1,2,3,4,5], dtype=int)
    print("Original array: ", end="")
    Array.iterate(array)
    print("After deletion: ", end="")
    Array.delete(array, 2, 5)
    current_size -= 1
    Array.iterate(array)