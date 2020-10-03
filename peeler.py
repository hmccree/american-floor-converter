def peeler(banana):
    if len(banana)<=2:
        print("that string is empty")
    else:
        i=len(banana)-1
        print(banana[1:i])

peeler("banana")
peeler("no")
peeler("thisisaverylongstring")