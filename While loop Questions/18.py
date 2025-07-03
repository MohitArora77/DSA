# Sum of Series -> 1/1*2 + 1/2*3 + 1/3*4 ... + 100

def series():
    sum=0
    i=1
    while(i<=100):
        sum+=1/i*(i+1)
        i+=1
    print(sum)

series() # 105.18737751763967

def series1():
    sum=0
    i=1
    while(i<=100):
        sum+=1/i*(i+1)
        i+=1
    return sum

Se=series1()
print(Se) # 105.18737751763967