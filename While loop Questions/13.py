# Sum of Series -> 1/1 + 1/2 + 1/3 + ...+ 1/100

def series():
    sum=0
    i=1
    while (i<=100):
        sum+=(1/i)
        i+=1
    print(sum)
series() # 5.187377517639621

# # With Return 

def series1():
    sum=0
    i=1
    while (i<=100):
        sum+=(1/i)
        i+=1
    return sum

Se=series1()
print(Se) # 5.187377517639621