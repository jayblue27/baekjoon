# 백준 - 센서 - 골드 5
'''
고속도로 위 N개의 센서 
집중국 -> N개의 센서들이 수집한 자료들을 모르고 분석

고속도로 위 최대 K개의 집중국을 세울 수 있다. 

N개의 센서가 적어도 하나의 집중국과는 통신이 가능해야 하며
유지비 문제로 각 집중국 수신 가능 영역의 길이의 합을 최소화 해야한다. 


입력
N = 센서의 개수 
K = 집중국의 개수
sensor_list = N개의 센서 좌표
'''

N = int(input())
K = int(input())
sensor_list = list(map(int, input().split()))

#센서 좌표 정렬
sensor_list.sort()

#센서간의 거리 확인 
distance = []
for i in range(N-1):
    distance.append(abs(sensor_list[i]-sensor_list[i+1]))

#거리 리스트를 정렬하고
distance.sort()

# 2개의 기지국일 경우 가장 멀리 있는 거리를 제거하면 가까운 애들끼리 묶여있는 효과발생
# K = 2 일때, 1
# K = 3 일때, 2 
# K 일때 K-1 만큼 pop 진행 후
# for _ in range(K-1):
#     distance.pop()

# 더한 결과값을 출력한다. 
print(sum(distance[:N-K]))