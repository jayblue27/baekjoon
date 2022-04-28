# 백준 - 세탁소 사장 동혁
# 알바 리암 거스름돈 주는 것을 실수
# 0.25, 0.1, 0.05, 0.01 잔돈 계산 

# 달러 잔돈 최소 코인개수 구하기
from collections import defaultdict

#입력
N = int(input())
cases = []
for _ in range(N):
    cases.append(int(input()))

# 1.24 -> 124, 0.25 -> 25로 표기함
# 입력값이 124로 나오니 동전 단위도 바꿔준다.
coin_lst = [25, 10, 5, 1]

coin_dict = defaultdict(str)

# 코인리스트 순회하면서 몫 =-> value , 나머지는 다음 coin list로 저장
for change in cases:
    for coin in coin_lst:
        coin_dict[coin] = str(change // coin)
        change -= ((change // coin) * coin)
    
    print(' '.join(coin_dict.values()))