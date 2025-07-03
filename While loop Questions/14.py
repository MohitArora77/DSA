# Sum of series  -> 1/2 + 1/4 + 1/6 ... + 1/100

def series():
    sum=0
    i=1
    while (i<=100):
        if i%2==0:
            sum+=1/i
        i+=1
    print(sum)

series() # 2.2496026691647115
 
# # With Return        
def series1():
    sum=0
    i=1
    while (i<=100):
        if i%2==0:
            sum+=1/i
        i+=1
    return sum
Se=series1()
print(Se) # 2.2496026691647115

