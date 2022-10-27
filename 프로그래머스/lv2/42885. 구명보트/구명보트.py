from collections import deque
def solution(people, limit):
    people.sort(reverse=True)
    people = deque(people)
    answer=0
    
    while people:
        tmp = people.popleft()
        if len(people) >=1 and limit-tmp >= people[-1]:
            people.pop()
        answer += 1
    return answer