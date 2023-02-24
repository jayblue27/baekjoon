'''
카드 길이가 각각 10개로 길지 않다
goal의 길이가 최대 10으로 card2 개의 원소를 전부 사용하지 않을수도 있다?

각각의 cards를 '큐'로 보고
goal 순환하면서 둘중에 하나 있으면 해당 카드뭉치 popleft
'''

from collections import deque
def solution(cards1, cards2, goal):
    n = len(goal)
    
    for i, w in enumerate(goal):
        if cards1 and w == cards1[0]:
            cards1.pop(0)
        elif cards2 and w == cards2[0]:
            cards2.pop(0)
        else:
            return 'No'
        print(cards1,cards2)
    
    return 'Yes'
        
    