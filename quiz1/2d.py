for c in range(30):
    for d in range(30):
        if(8*c+d)%30==4 and (26*c+d)%30==10 and (7*c+d)%30 == 27:
            print(c,d)