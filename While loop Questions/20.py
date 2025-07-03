# Accept 2 number from the user a,b (a to power b)

def pow(a,b):
    pow=1
    i=1
    while(i<=b):
        pow*=a
        i+=1
    print(pow)
pow(3,3) # 27