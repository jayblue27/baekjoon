#백준 - 잃어버린 괄호
#마이너스 뒤의 값이 가장 크게 나와야함
a = input()
# 마이너스로 먼저 쪼갰다.
a = a.split('-')

s = 0
# 첫번째 뭉치 합 구하기
for i in a[0].split('+'):
    s += int(i)

# 두번째 뭉치 숫자에서 뺴주기
for i in a[1:]:
    for j in i.split('+'):
        s -= int(j)

print(s)