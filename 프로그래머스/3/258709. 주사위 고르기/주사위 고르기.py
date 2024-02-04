'''
1. 문제이해
- n개의 주사위로 A와 B가 경쟁
- 각각 n/2개의 주사위 가져가서 굴려서 나온합이 큰 경우 이김
- A가 승리할 확률이 높으려면 몇번 몇먼의 주사위를 가져가야 하는가?

- dice의 길이는 최대 10개
- 각 주사위는 6개의 면

- 최대 5개 10C5 (252) * 6C1 (6) / 5! 

2. 접근방법
- 
- 주사위 개수 세기 -> n = len(dice)
- 몇개의 주사위를 골라야 하는지 계산 -> n//2 개 

- 경우의 수는 어떻게 계산해야 하는가? -> 핵심
  - 

'''

# def solution(dice):
#     answer = []
#     return answer

from itertools import combinations, product

def solution(dices):
    dp = {}
    L = len(dices)
    for A_index_combi in combinations(range(L), L//2):
        B_index_combi = [i for i in range(L) if i not in A_index_combi]

        A, B = [], []
        for order_product in product(range(6), repeat=L//2):
            A.append(sum(dices[i][j] for i, j in zip(A_index_combi, order_product)))
            B.append(sum(dices[i][j] for i, j in zip(B_index_combi, order_product)))

        B.sort()

        wins = 0
        for num in A:
            left, right = 0, len(B)-1
            while left <= right:
                mid = (left + right)//2
                if num <= B[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            wins += left

        dp[wins] = list(A_index_combi)

    max_key = max(dp.keys())

    return [x+1 for x in dp[max_key]]