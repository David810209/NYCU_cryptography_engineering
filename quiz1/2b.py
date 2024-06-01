while True:
    x = int(input())
    f = False
    for i in range(1,30):
        if(x*i)%30 == 1:
            print(str(x)+'->'+str(i))
            f = True
            break