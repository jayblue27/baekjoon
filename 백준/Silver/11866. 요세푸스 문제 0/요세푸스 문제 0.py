# 백준세푸스 문제 0

# 요세푸스 순열
# 원형

#입력
#N명의 사람, K번째의 사람 제거
N, K = map(int, input().split())
lst = [i for i in range(1,N+1)]


ans = []
idx = 0
# N명의 사람이 제거될 때까지 계속 
for _ in range(N):
    idx += K-1
    # 리스트의 길이가 index number보다 작거나 같으면
    if idx >= len(lst):
        # 인덱스 번호를 길이만큼 나눈 나머지로 변경해준다.
        idx = idx%len(lst)
    #출력형태에 맞추기 위해서 str로 입력 받음
    ans.append(str(lst.pop(idx)))

#출력
print(f"<{', '.join(ans)}>")