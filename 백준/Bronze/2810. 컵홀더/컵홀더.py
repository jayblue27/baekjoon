#백준 - 컵홀더

#입력
N = int(input())
seat = input()

# 커플석 LL -> X로 변환
seat = seat.replace('LL', 'X')

#커플석이 있을경우 seat 길이 +1
if 'X' in seat:
    print(len(seat)+1)
#커플석이 없으면 모든사람 팔걸이 사용 가능(seat 길이만큼)
else:
    print(len(seat))