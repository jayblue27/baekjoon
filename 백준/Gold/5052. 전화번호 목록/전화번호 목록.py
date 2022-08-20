#백준 - 전화번호 목록 - 골드 4
'''
t = 테스트 케이스 수 (1<=t<=50)
n = 전화번호의 수(1<=n<=10000)
n개의 전화번호 (길이 10자리 이하)
* n개의 전화번호 중 중복값은 없다. 

일관성이 없는경우(일부의 값으로 시작하는 경우) : NO 출력
일관성이 있는경우(모든 전화번호가 서로 간섭이 없는경우) : YES 출력
'''
import sys
input = sys.stdin.readline

#입력
t = int(input().rstrip())  # t : 테스트 케이스
for _ in range(t):
    n = int(input().rstrip()) # n : 전화번호의 수
    tel_nums = []
    # 전화번호부 생성
    for _ in range(n):
        tel_nums.append(input().rstrip())
    
    # 정렬
    tel_nums.sort()

    # 일관성 확인
    for i in range(len(tel_nums)-1):
        if tel_nums[i+1].startswith(tel_nums[i]):
            print('NO')
            break
    else:
        print('YES')