n = input()


def gen_making(n):
    lst = [int(n)]
    for i in range(len(n)):
        lst.append(int(n[i]))
    
    return sum(lst)

# 숫자 순회 입력 숫자 까지
for i in range(int(n)):
    # 자릿수 순회 (길이만큼)
    if gen_making(str(i)) == int(n):
        print(i)
        break
else:
    print(0)