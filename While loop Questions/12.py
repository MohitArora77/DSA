# Sum of Series -> 1^2*2 + 2^2*3 + 3^2*4 + 1... +100

def series():
    sum=0
    i=1
    while(i<=100):
        sum+=(i**2)*(i+1)
        i+=1
    print(sum)
series() # 25840850

# # With Return
def series1():
    sum=0
    i=1
    while(i<=100):
        sum+=(i**2)*(i+1)
        i+=1
    return sum
Se=series1()
print(Se)   # 25840850

      
        