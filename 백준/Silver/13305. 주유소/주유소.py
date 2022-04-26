# 백준 - 주유소 - 그리디

# N개의 도시 -> 일직선 도로 위
# 제일 왼쪽에서 오른쪽으로 이동
# 인접한 두 도시의 도로길이는 같을수도 다를수도 있다.

# 처음 출발시 기름 x
# 기름통 크기 무제한
# 1km/1리터 

#입력
N = int(input())
distances = list(map(int, input().split()))
prices = list(map(int, input().split()))


# 17점 짜리 풀이

#맨 마지막 도시의 기름값은 의미 없으므로 제외한 리스트를 생성한다
# new_prices = prices[:-1]

# ans = 0
# for i in range(len(new_prices)):
#     #현재 도시의 기름값이 최소값이면 남은 거리를 이동할 만큼 기름을 다 채워버림
#     if new_prices[i] == min(new_prices):
#         ans += sum(distances[i:]) * new_prices[i]
#         break
#     # 그 외에는 다음도시 갈만큼만 넣는다.
#     else:
#         ans += distances[i] * new_prices[i]

# print(ans)

# 와 .... 이게 그리디지 ..
ans = 0
min_price = prices[0]

for i in range(N-1):
    if prices[i] < min_price:
        min_price = prices[i]

    ans += min_price * distances[i]

print(ans)