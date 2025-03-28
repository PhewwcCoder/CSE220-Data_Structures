"""
Given a non-negative int n, return the sum of its digits recursively (no loops). Note that mod (%)
by 10 yields the rightmost digit (126 % 10 is 6), while divide (/) by 10 removes the rightmost digit
(126 / 10 is 12)."""

# def sumDigits(n):
#     if n==0:
#         return 0
#     return n%10+ sumDigits(n//10)
# print(sumDigits(1))
# print(sumDigits(49))
# print(sumDigits(126))


"""We have bunnies standing in a line, numbered 1, 2, ... The odd bunnies (1, 3, ..) have the
normal 2 ears. The even bunnies (2, 4, ..) we'll say have 3 ears, because they each have a
raised foot. Recursively return the number of "ears" in the bunny line 1, 2, ... n (without loops or
multiplication)."""

# def bunnyEars2(n):
#     if n==0:
#         return 0
#     if n%2!=0:
#         return 2+ bunnyEars2(n-1)
#     else:
#         return 3+ bunnyEars2(n-1)
# print(bunnyEars2(0))
# print(bunnyEars2(1))
# print(bunnyEars2(2))


"""Given an array of ints, compute recursively the number of times that the value 11 appears in the
array. We'll use the convention of considering only the part of the array that begins at the given
index. In this way, a recursive call can pass index+1 to move down the array. The initial call will
pass in index as 0."""

# def array11(arr,index):
#     if index==len(arr):
#         return 0
#     else:
#         if arr[index]==11:
#             return 1+array11(arr,index+1)
#         return array11(arr,index+1) 
# print(array11([1,2,11],0))
# print(array11([11, 11], 0))
# print(array11([1, 2, 3, 4], 0))


"""Given a string, compute recursively (no loops) a new string where all appearances of "pi" have
been replaced by "3.14"."""

# def changePi(string):
#     if len(string)==2 and string[-2:]=="pi":
#         return "3.14"
#     if len(string)==1:
#         return string
#     if string[0:2]=="pi":
#         return "3.14"+changePi(string[2:])
#     else:
#         return string[0]+changePi(string[1:])
# print(changePi("xpix"))
# print(changePi("pipi"))
# print(changePi("pip"))
# print(changePi("i"))


"""Given a string that contains a single pair of parenthesis, compute recursively a new string made
of only of the parenthesis and their contents, so "xyz(abc)123" yields "(abc)"."""

def parenBit(s):
    if s[0]=="(":
        if s[-1]==")":
            return s
        else:
            return parenBit(s[:-1])
    return parenBit(s[1:])
print(parenBit("xyz(abc)123"))
print(parenBit("x(hello)"))
print(parenBit("(xy)1"))
