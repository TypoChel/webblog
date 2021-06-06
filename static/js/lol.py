i=780500
counter = 0
while counter <5:
    maxi = -100
    mini = 100000000000000
    for j in range(2,i):
        if i%j == 0 and j%2 != 0:
            if maxi < j:
                maxi = j
            if mini > j:
                mini = j
    if maxi-mini != 0 and (maxi-mini)%7==0:
        counter += 1
        print(i," ",maxi-mini)
    i+=1