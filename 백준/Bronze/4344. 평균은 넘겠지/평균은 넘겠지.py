# 테스트 케이스의 갯수 C
C = int(input())
# N 및 N명의 점수

tmp = []
for i in range(C):
    N = list(map(int,input().split()))
    
    tmp_avg = sum(N[1:]) / N[0]

    count = 0    
    for j in N[1:]: 
        if j > tmp_avg:
            count += 1
    
    ovr = (count / N[0]) *100
    tmp.append(ovr)

for i in tmp:
    print(f'{i:.3f}%')