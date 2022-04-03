while True:
    n = input()  
    #0값 입력시 종료
    if n == '0':
        break

    else:
        if n == n[-1::-1]:
            print('yes')
        else:
            print('no')