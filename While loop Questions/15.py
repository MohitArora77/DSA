# Sum of Series -> 1/1 + 1/3 + 1/5 + ....+ 1/100 (only Odd)

def series():
    sum=0
    i=1
    while (i<=100):
        if i%2!=0:
            sum+=1/i
        i+=1
    print(sum)
series() # 2.937774848474907

# # With Return

def series1():
    sum=0
    i=1
    while(i<=100):
        if i%2!=0:
            sum+=1/i
        i+=1
    return sum

Se=series1()
print(Se) # 2.937774848474907

