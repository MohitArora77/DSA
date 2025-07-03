from array import *
val=array('i',[5,-9,4,3,2]) # can store interger in -ve and +ve
# print(val)

# TO copy the one array in another 

# val2=array(val.typecode,(a for a in val))
# print(val2)

# To take user input inside the empty array
# val2=array('i',[])
# n=int(input("Enter the length:"))
# for i in range(n):
#     x=int(input("Enter the data :"))
#     val2.append(x)
# print(val2)

#  To take user input inside the empty array and search for the index by users.
val2=array('i',[])
n=int(input("Enter the length: "))
for i in range(n):
    x=int(input("Enter the data :"))
    val2.append(x)
print(val2)
n1=int(input("Enter the number to find the index position :"))
for i in val2:
    y=val2.index(n1)
print(y)
