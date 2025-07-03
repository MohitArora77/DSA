
# Ques -> Sum of all even number from 1 to 100 using function (without return statement)

def evenfunc():
    sum=0
    i=1
    while(i<=100):
        if i%2==0:
            sum+=i
        else:
            pass
        i+=1
    print(sum,end=" ")
        
evenfunc() # 2550 

# # With return

def evennum():
    sum=0
    i=1
    while(i<=100):
        if i%2==0:
            sum+=i
        else:
            pass
        i+=1
    return sum

evensum=evennum()
print(evensum) # 2550
    

            