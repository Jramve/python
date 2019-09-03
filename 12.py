num = int(input("number: "))
if num < 0:
    print("no neg")
else:
    for i in range(num):
        if i % 2 != 0:
            print (i,end=",")
    
