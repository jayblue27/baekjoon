'''
## 1번 12번 제외 시간초과 ;;
for로 mid 움직이면서 
좌우 set의 len을 비교
동일하면 answer +=1

매번 set len을 해야해서 시간 초과 발생
'''
# def solution(topping):
#     answer = 0
    
#     left = set(topping[:1])
#     right = set(topping[1:])
        
#         # 가지치기 1
#         if left > right:
#             break
        
#         if left == right:
#             answer+=1
    
#     return answer


def solution(topping):
    passed1, passed2 = set(), set()
    check1, check2 = [], []
    for each in topping:
        passed1.add(each)
        check1.append(len(passed1))
    for each in topping[::-1]:
        passed2.add(each)
        check2.append(len(passed2))
    check2 = check2[::-1]  # check2.reverse()
    return sum(1 for index in range(len(check1) - 1) if check1[index] == check2[index + 1])        
