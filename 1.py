# Array 

# import array as arr 

# arr.array([1,2,3,4,5])

# To create a array :
# from array import *

# To store the value inside that array :

# val=array('i',[5,-9,4,3,2]) # can store interger in -ve and +ve
# print(val)

# from array import *
# val2=array('i',[1,2,3,4])
# val2=array('I',[1,2,3,-4]) # overflow error : can't convert the negative value to unsigned int

# print(val2.buffer_info) # <built-in method buffer_info of array.array object at 0x00000166EA850540>
# print(val2.buffer_info()) # (2109124936352, 4)
# print(val2.typecode)  # i

# To reverse :
# print(val2.reverse()) # None : because reverse() : don't return the value.
# val2.reverse()
# print(val2) # array('i', [4, 3, 2, 1])

# Want to print the value one by one (specific)
# print(val2)
# print(val2[3]) # 4

# If we want to print all the values one by one . ( if we know length)
# for i in range(0,4): 
#     print(val2[i],end=" ") # 1 2 3 4
    
# if we don't know the length of value ?
# for i in range(0,len(val2)):
#     print(val2[i],end=" ") # 1 2 3 4

# Can also use the variable itself
# for i in val2:
#     print(i,end=" ") # 1 2 3 4 

# To interact with characters
# val3=array('u',['a','e','i'])
# print(val3)
# for i in val3:
#     print(i,end=" ") # a e i
 
# # to be able to create a newarray with previous array :
   
# newarray=array(val2.typecode,(a for a in val2))
# # print(newarray) # array('i', [1, 2, 3, 4])

# if we want the value to be in square
# newarray1=array(newarray.typecode,(a**2 for a in newarray))
# print(newarray1) # array('i', [1, 4, 9, 16])

# i=0
# while i<len(newarray1):
#     print(newarray1[i],end=" ") # 1 4 9 16
#     i+=1 

# EXCERCISE :

# 1. Create an array where values will be coming from the user
# from array import *
# arr=array('i',[])

# n=int(input("Enter the length of the array:"))
# for i in range(n):
#     x=int(input("Enter the length of the array:"))
#     arr.append(x)

# print(arr)

# 2 . How to take user input in Array
# from array import *
# arr=array('i',[])

# n=int(input("Enter the length of the array :"))
# for i in range(n):
#     x=int(input("Enter the Data :"))
#     arr.append(x)
# print(arr) # array('i', [1, 2, 3, 4])

# # 3. Ask the user for the value and search for the index.
# from array import *
# arr1=array('i',[])
# n=int(input("Enter the length: "))
# for i in range(n):
#     x=int(input("Enter the data :"))
#     arr1.append(x)
# print(arr1)

# #  now take a value for the user and search its index number. (using index())
# # n1=int(input("Enter the number:"))
# # for i in arr1:
# #     y=arr1.index(n1)

# # print(y)

# # without using index function
# n2=int(input("enter the number :"))
# y=[]
# for i in range(len(arr1)):
#     if arr1[i]==n2:
#         y=i
# print(y)


# Create a new array with user input and also search the index according to the user.
# from array import *
# arr1=array('i',[])
# n=int(input("Enter the length:"))
# for i in range(n):
#     x=int(input("Enter the data:"))
#     arr1.append(x)
#     # arr1.append(x*x)
# print(arr1) # array('i', [1, 2, 3, 4, 5])

# # n1=int(input("Enter the index value:"))
# # for i in range(len(arr1)):
# #     if arr1[i]== n1:
# #         y=i
# #     else:
# #         pass
# # print(y)

# # index()
# n1=int(input("Enter the index value:"))
# for i in arr1:
#     y=arr1.index(n1) # able to get index position
# print(y) # 1 
    
# create a new array using old array .
# from array import *
# arr1=array('i',[1,2,3,4,5])
# print(arr1) # array('i', [1, 2, 3, 4, 5])
# newarr1=array(arr1.typecode,(a for a in arr1))
# print(newarr1) # array('i', [1, 2, 3, 4, 5])
# newarr1=array(arr1.typecode,(a*a for a in arr1))
# print(newarr1) # array('i', [1, 4, 9, 16, 25])

