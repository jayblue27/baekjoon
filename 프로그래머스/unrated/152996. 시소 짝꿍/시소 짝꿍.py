'''
시소 짝궁

중심으로부터 
2,3,4 -> 3가지의 지점

n^2이면 시간초과
- 궁금한점 중복은 처리해야하나?


Counter로 숫자(key), 개수(counts)

1. 숫자가 같은경우 +1
- key의 value가 2 이상일때 

2. 1:2(2배)인 경우 +1
- key(본인)값의 2배인 숫자가 하나이상 있는 경우

3. 2:3(1.5배) 인 경우 +1
- key(본인)값의 1.5배 숫자 하나이상

4. 3:4(??배)인 경우
- 본인값이 3으로나눈값이 0 and 대상이 4로 나눈 값이 0인경우 
'''
from collections import Counter

# def solution(weights):
#     answer = 0
#     dic = Counter(weights)
#     arr = [int(x/4) for x in dic.keys()]
#     for k, v in dic.items():
#         if dic[k] >= 2:
#             answer+= dic[k]-1
#         if 2*k in dic.keys():
#             answer+=1
#         if 1.5*k in dic.keys():
#             answer+=1
#         if k/3 in arr:
#             answer+=1
#     return answer

from collections import Counter
def solution(weights):
    # breakpoint()
    answer = 0
    people_counter = Counter(weights)
    for weight, num_of_people in people_counter.items():
        answer += num_of_people * (num_of_people - 1) // 2
        for dis1, dis2 in [(2, 3), (2, 4), (3, 4)]:
            answer += people_counter[weight * dis1 / dis2] * num_of_people
    return answer
