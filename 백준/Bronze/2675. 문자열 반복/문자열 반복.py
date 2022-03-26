#S 입력 받아
#각 문자를 R번 반복한 새문자열 P 만들어 출력

S = int(input())

tmp_list = []
for i in range(S):
    R, T = input().split()
    
    tmp = ''
    for j in T:
        tmp = tmp+(j*int(R))
    
    tmp_list.append(tmp)    

for i in tmp_list:
    print(i)
