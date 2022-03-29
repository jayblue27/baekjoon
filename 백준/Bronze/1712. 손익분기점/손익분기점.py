A, B, C = map(int, input().split())

# 가변비 B 보다 판매가가 많으면 손익분기를 달성할 수 없다. 
if B>=C:
    print(-1)   
else:
    print(int(A/(C-B)+1))
