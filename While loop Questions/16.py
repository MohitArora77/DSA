# Sum of Series -> 1/1^2 + 1/2^2 + 1/3^2 ... + 1/100^2

def series():
    sum=0
    i=1
    while(i<=100):
        sum+=1/(i**2)
        i+=1
    print(sum)
    
series() # 1.6349839001848923

# # With Return
def series1():
    sum=0
    i=1
    while(i<=100):
        sum+=1/(i**2)
        i+=1
    return sum
Se=series1()
print(Se) # 1.6349839001848923

