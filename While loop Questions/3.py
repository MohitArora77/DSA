
# Ques -> Sum of all  odd number from 1 to 100 using function (without return statement)

def oddnum():
    sum=0
    i=1
    while(i<=100):
        if i%2!=0:
            sum+=i
        else:
            pass
        i+=1
    print(sum)
    
oddnum() # 2500

# # With return
def oddnum1():
    sum=0
    i=1
    while(i<=100):
        if i%2!=0:
            sum+=i
        else:
            pass
        i+=1
    return sum

oddnumber=oddnum1()
print(oddnumber) # 2500