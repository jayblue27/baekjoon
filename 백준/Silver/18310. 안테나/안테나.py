# 안테나 - 실버3
'''
일직선 상 마을 여러채 집 
안테나로부터 모든 집까지 거리의 총 합이 최소
안테나는 집이 있는 곳에만 설치 가능
동일 위치에 여러 집 존재 가능

집들의 위치값 주어질때, 안테나 설치 위치 선택
여러개면 작은 수

'''
# n = 4
# houses = [1, 5, 7, 9]

# # 시간 초과 걱정 - 역시 시간초과 O(n^2)
# n = int(input())
# houses = list(map(int,input().split()))
# tmp = [0] * len(houses)

# for i in range(len(houses)):    
#     for j in range(len(houses)):
#         if i == j:
#             continue
#         else:
#             tmp[i] += abs(houses[j] - houses[i])

# idx = tmp.index(min(tmp))
# print(houses[idx])


# # 0 -1 가운데서 가장 가까운 수
# # 최적해 보장하는지 잘 모르겠다 -> 틀렸다
# n = int(input())
# houses = list(map(int,input().split()))
# houses.sort()
# tmp_val = (houses[-1] - houses[0]) // 2
# tmp_arr = [0] * len(houses)

# for i in range(len(houses)):
#     tmp_arr[i] = abs(houses[i] - tmp_val)

# idx = tmp_arr.index(min(tmp_arr))
# print(houses[idx])


# n-1 // 2 
'''
그리고 실제 코드로는 
위 두 경우를 굳이 나눌 필요없이 크기를 2로 나눈 몫을 이용하면 된다. 
단, 이때 크기를 먼저 1로 뺴준다. 
그 이유는 홀수일 때는 어차피 나머지가 1이므로 값이 같고, 
짝수일 때 그냥 2로 나누면 오른쪽에 위치한 집의 값이 나온다.
(6을 2로 나누면 3이니까) 
따라서 다음에 -1을 해줘야 하는데 이러면 홀수일 때를 
따로 또 분리해 줘야 하므로 애초에 크기보다 1 작은 값을 2로 나누면 해결되는 아이디어다.
'''
n = int(input())
houses = list(map(int,input().split()))
houses.sort()
print(houses[(n-1)//2])