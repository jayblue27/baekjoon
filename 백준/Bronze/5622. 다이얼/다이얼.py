# 1 : 2초
# 2 : ABC 

#dict로 각 알파벳이 걸리는 시간을 지정
tmp = {'abc':3, 'def':4,'ghi':5,'jkl':6,'mno':7,'pqrs':8,'tuv':9,'wxyz':10}
S = input().lower()

time = 0

#해당 알파벳이 key값에 있을때 value값을 변수에 더해준다.
for i in S:
    for abc, sec in tmp.items():
        if i in abc:
            time += sec
print(time)