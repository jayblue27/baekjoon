# 알바생 강호
'''
8시가 될 때까지 줄 세우기
8시 되는순간 입구에서 커피 하나씩 받고 자리로 간다. 

손님들 강호에게 팁 준다.
팁 -> 손님들이 커피 몇 번째 받는지(=입장 몇 번째 하는지)에 따라 다른 액수로 준다. 
원래 주려고 했던 돈 - (등수 - 1) ※만약 음수라면 팁을 못 받는다
(등수 -1) 은 index와 같음

손님의 순서를 적절히 바꿔 팁을 최대로 받을 수 있게 하라 

N명의 대기 중인 사람 수 (<= 100,1000)
N명의 팁

원래 주려고 했던 돈이 크면 좋다
등수가 빠르면 좋다.
-> 큰 돈 주려고 한사람을 먼저 세운다. 

값이랑 index -> enumerate로 한번에 계산 가능
'''
import sys
input = sys.stdin.readline

n = int(input())
tips = []
for _ in range(n):
    tips.append(int(input()))

tips.sort(reverse=True)

# 팁계산 
ans = 0
for i, v in enumerate(tips):
    # 계산식이 값이 양수인 경우에만 더해준다.
    if v - i > 0:
        ans += v-i

print(ans)