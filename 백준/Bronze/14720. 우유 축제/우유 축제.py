#백준 - 우유축제 - 브론즈3

'''
딸기(0), 초코(1), 바나나 우유 (2)
딸기우유 -> 초코우유 -> 바나나우유 -> 딸기우유

milk 변수 
0부터 하나씩 

milk = 0
for i in 우유가게:
    if i == milk%3:
        milk += 1
print(milk)

'''
#입력
N = int(input())
shops = list(map(int,input().split()))

#출력
milk = 0
for i in shops:
    # 해당 순서의 우유만 섭취
    # 0 -> 1 -> 2 -> 0 ... 순서이므로 3으로 나눈 나머지를 이용한다.
    if i == milk % 3: # 우유종류 3가지 
        milk += 1

print(milk)