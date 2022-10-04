# 콘테스트 - 브론즈2
'''
첫 열줄 받아서 첫 리스트
두번째 열줄 받아서 두번째 리스트

각 리스트의 상위 3명의 합을 출력
'''
ans_1 = []
ans_2 = []
for i in range(20):
    if i < 10:
        ans_1.append(int(input()))
    else:
        ans_2.append(int(input()))

ans_1.sort(reverse=True)
ans_2.sort(reverse=True)

print(sum(ans_1[:3]), sum(ans_2[:3]))