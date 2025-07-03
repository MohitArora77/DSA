# Assignment -2

# Ques -> Sum of all natural number from 1 to 100 using function (without return statement)

def natnum():
    sum=0
    i=1
    while i<=100:
        sum+=i
        i+=1
    print(sum) 

natnum() # 5050

# # With return statement
def numfunc():
    sum=0
    i=1
    while(i<=100):
        sum+=i
        i+=1
    return sum

naturalnum=numfunc()
print(naturalnum) # 5050