# Sum of Series -> 1/1^3 + 1/2^3 + 1/3^3 ... + 1/100^3

def series():
    sum=0
    i=1
    while(i<=100):
        sum+=1/(i**3)
        i+=1
    print(sum)
series() # 1.2020074006596781

# # with Return

def series1():
    sum=0
    i=1
    while(i<=100):
        sum+=1/(i**3)
        i+=1
    return sum
Se=series1()
print(Se) # 1.2020074006596781

