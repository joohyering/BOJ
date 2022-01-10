
pelInput = input()
while (pelInput != '0') :
    pel = pelInput[::-1]
    if pel == pelInput :
        print('yes')
    else:
        print('no')
    pelInput = input()

