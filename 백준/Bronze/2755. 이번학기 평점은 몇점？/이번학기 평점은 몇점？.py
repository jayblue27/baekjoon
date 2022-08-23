# 이번학기 평점은 몇점? - 백준 - 브론즈1
'''
과목 학점 성적 주어졌을때 평점 계산
'''
# 준비
grade_table = {'A+':4.3, 'A0':4.0, 'A-':3.7,
                'B+':3.3, 'B0':3.0, 'B-':2.7,
                'C+':2.3, 'C0':2.0, 'C-':1.7,
                'D+':1.3, 'D0':1.0, 'D-':0.7,
                'F':0.0}

credit = 0
total = 0

# 입력 및 계산 (총 학점 및 주어진 계산식)
N = int(input())
for _ in range(N):
    i,j,k = list(input().split(' '))
    total += int(j) * grade_table[k]
    credit += int(j)   
    
# 결과 출력 
print('{:.2f}'.format(round(total/credit+10**-10, 2)))