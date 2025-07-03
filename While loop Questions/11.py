# Sum of the Series -> 1*2^2 + 2*3^2 + 3*4^2 ....+ 100

def series():
    sum=0
    i=1
    while(i<=100):
        sum+=i*(i+1)*(i+1)
        i+=1
    print(sum)
    
series() # 26184250

def series1():
    sum=0
    i=1
    while(i<=100):
        sum+=i*(i+1)**2
        i+=1
    print(sum)
    
series1() # 26184250

# # With Return
def series2():
    sum=0
    i=1
    while(i<=100):
        sum+=i*(i+1)**2
        i+=1
    return sum
    
Se=series2()
print(Se) # 26184250