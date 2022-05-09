import sys
input = sys.stdin.readline

#입력
D,B = map(int, input().split())
D_list = [] # 듣도 못한 리스트
B_list = [] # 보도 못한 리스트
for _ in range(D):
    D_list.append(input().strip())
for _ in range(B):
    B_list.append(input().strip())

#교집합 구하기 및 오름차순 정렬
ans = list(set(D_list) & set(B_list))
ans.sort()

#출력
print(len(ans))
for i in ans:
    print(i)