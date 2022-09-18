for _ in range(int(input())):
    dic = {}
    for i in range(int(input())):
        v, k = input().split()
        if k not in dic:
            dic[k] = 1
        else:
            dic[k] += 1
    ans = 1
    for value in dic.values():
        ans *= (value + 1)
    print(ans - 1)