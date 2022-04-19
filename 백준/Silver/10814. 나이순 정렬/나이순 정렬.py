#백준 - 나이순 정렬 - 정렬

## 입력
# N: 회원의 수 
# 나이와 이름 

N = int(input())
members = []
for i in range(N):

    members.append(input().split())

# 나이순 정렬
# 나이가 같으면 가입한 순으로
members.sort(key=lambda x:int(x[0]))
for age, name in members:
    print(age, name)