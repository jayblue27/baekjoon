#입력 5자리 숫자
val_nums = list(map(int, input().split()))
#리스트 원소 제곱
val_nums = [i**2 for i in val_nums]
# 합을 10으로 나눈 나머지
num = sum(val_nums) % 10
#출력
print(num)