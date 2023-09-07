'''
1. 문제이해
- 한 row에 하나의 땅을 밟으면서 내려오는데
- 끝까지 내려왔을때 가장 큰 값이 되게 하는 경우

2. 접근방법
- 단순히 생각하면 각 row의 max값을 더하고
- 다음 row의 max값을 찾아서 더하면 된다고 생각
- index 겹치면 해당 값 제외한 max 값

- 근데 그리디 한 방법으로 풀면 안될 것 같음 
- dp로 풀어야 함?

- ex
    5 (x)
    1 2 3   -> 3
    1 2 8   -> 2 

    10 (o)
    1 2 3   -> 2
    1 2 8   -> 8

- if r번째 max값의 index와 r+1번째 max값의 index값이 같다면
- r번째 2번째 최고값 + r+1번째 1번째 최고값

- r번째 row의 1번째 큰값 및 index 2번째 큰값 및 index 구하고
- r+1번째 row의 1번째 큰값 및 index 2번째 큰값 및 index 구한다음
- if r번째 index == r+1번째 index 면 두 값중에 큰 값을 넣고 현재 index로 지정 

3. 오답노트
- 쉽게 생각했는데 너무 오래 걸린다. 
- 
'''


# def solution(land):
#     answer = 0
    
#     # 현재 row 맥스값, 맥스값의 idx   
#     r_max = sorted(land[0], reverse=True)[0]
#     r_max_idx = land[0].index(r_max)
    
#     r_2nd = sorted(land[0], reverse=True)[1]
#     r_2nd_idx = land[0].index(r_2nd)
    
#     for r in range(1, len(land)):
#         nr_max = sorted(land[r], reverse=True)[0]
#         nr_max_idx = land[r].index(nr_max)
    
#         nr_2nd = sorted(land[r], reverse=True)[1]
#         nr_2nd_idx = land[r].index(nr_2nd)
        
#         # r번째 max idx와 r+1번째 max idx값이 같은경우
#         if r_max_idx == nr_max_idx:
#             # 이전의 2번째 + 이번의 1번째 > 이전의 1번째 + 이번의 2번째 -> 이번의 값으로 max_idx를 갱신
#             if 
    
# 참고 - 54분 소요
# https://wookcode.tistory.com/109
# dp로 접근
# 각자의 자리에 본인 자리를 제외한 이전값의 max값과 더한 값을 갱신
def solution(land):
    answer = 0
    for i in range(1,len(land)):
        land[i][0] += max(land[i-1][1], land[i-1][2], land[i-1][3])
        land[i][1] += max(land[i-1][0], land[i-1][2], land[i-1][3])
        land[i][2] += max(land[i-1][0], land[i-1][1], land[i-1][3])
        land[i][3] += max(land[i-1][0], land[i-1][1], land[i-1][2])
    return max(land[-1])

# 위 코드를 좀 더 간단하게 
# def solution(land):
#     for i in range(1,len(land)):
#         for j in range(len(land[0])):
#             land[i][j] += max(land[i-1][:j] + land[i-1][j+1:])
#     return max(land[len(land)-1])
