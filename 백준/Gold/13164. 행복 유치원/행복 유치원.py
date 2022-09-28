# 행복 유치원 - 골드 5
'''
N명의 원생
키 순서대로 세우고
K개의 조로 나눈다. 

가장 큰 학생, 작은학생의 차이만큼 비용이 든다. 
K개의 조 비용의 합을 최소로 하는 법

숫자 간 차이구한다음
내림차순 정렬
k-1개 만큼 갭이 큰 애들을 단독 그룹으로 만들어서 비용을 최대한 줄이고
나머지 1개의 그룹에 갭이 작은 애들을 몰아 넣는다.

'''

n, k = map(int, input().split())
heights = [*map(int, input().split())]

diff = []
for i in range(1, len(heights)):
    diff.append(heights[i] - heights[i-1])

diff.sort(reverse=True)

print(sum(diff[k-1:]))
