for a in range(30):
    for b in range(30):
        if(4*a+b)%30==8 and (10*a+b)%30==26 and (27*a+b)%30 == 7:
            print(a,b)