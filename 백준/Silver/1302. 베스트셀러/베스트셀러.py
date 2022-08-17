# 백준 - 베스트셀러 - 실버 4
'''
하루 동안 팔린 책의 제목 - 입력
가장 많이 팔린 책의 제목을 출력
(만약 가장 많이 팔린게 여러개면 사전순으로)

리스트로 입력 받고
Counter 함수로 counting하고 most_common 이용해서 결과값 찾기
'''
from collections import Counter

#입력
N = int(input())
arr = []

for _ in range(N):
    arr.append(input())

arr = Counter(arr)

top_seller = max(arr.values()) # 가장 많이 팔린 책 권수


best_arr = [] # 가장 많이 팔린 책 목록
for k, v in arr.items():
    if v == top_seller:
        best_arr.append(k)

best_arr.sort() # 정렬
print(best_arr[0])