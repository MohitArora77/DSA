# sum of below series 1*2 + 2*3 + 3*4 +...100

def series():
    sum=0
    i=1
    while i<=100:
        sum+=i*(i+1)
        i+=1
    print(sum)
    
series() # 343400

# # with return

def series1():
    sum=0
    i=1
    while(i<=100):
        sum+=i*(i+1)
        i+=1
    return sum

Se=series1()
print(Se) # 343400