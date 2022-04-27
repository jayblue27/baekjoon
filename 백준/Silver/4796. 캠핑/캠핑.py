#백준 - 캠핑 

# 수학규칙이 있을거 같아서 봤다. 
# 1 2 3 4 5 6 7 8 / 9 10 11 12 13 14 15 16 / 17 18 19 20
# 1 1 1 1 1 1 1 1 / 2  2  2  2  2  2  2  2 /  3  3  3  3   # 연속 몇일 중    P
#                                                          # 몇일동안만 가능 L
# V: 베케이션
# 점화식
# (V // P) * L + (V % P)

tmp = []
while True:
    L, P, V = map(int, input().split())
    if L == 0 and P == 0 and V == 0:
        break
    # 계산식
    # 나머지 부분이 L을 넘으면 L로 퉁친다.
    if V % P > L:
        ans = ((V // P) * L) + L 
    else:
        ans = ((V // P) * L) + (V % P)

    tmp.append(ans)
    
for i in range(len(tmp)):
    print(f"Case {i+1}: {tmp[i]}")