# Sum of Square of all even numbers from 1 to 100 with using function

def sqeven():
    sum=0
    i=1
    while(i<=100):
        if i%2==0:
            sum+=i**2
        else:
            pass
        i+=1
    print(sum)
    
sqeven() # 171700

# # With return
def sqeven1():
    sum=0
    i=1
    while i<=100:
        if i%2==0:
            sum+=i**2
        else:
            pass
        i+=1
    return sum

Se=sqeven1()
print(Se) # 171700
        
        