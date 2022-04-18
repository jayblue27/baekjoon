from collections import Counter
import sys

#입력
input = sys.stdin.readline
N = int(input())
nums = []
for _ in range(N):
    nums.append(int(input()))



# 정렬
nums.sort()

#1. 산술평균 : sum // N
ans1 = int(round(sum(nums) / N, 0))

#2. 중앙값 : 정렬 후, 인덱스의 정 중앙
ans2 = nums[N//2]

#3. 최빈값 : 딕셔너리? , 여러개 있을때에는 최빈값중 두번째로 작은 값
# 카운트 
count_list = []
count_list = Counter(nums).most_common()
if len(count_list) > 1 and count_list[0][1] == count_list[1][1]: #최빈값 2개 이상
    ans3 = count_list[1][0]
else:
    ans3 = count_list[0][0]

#4. 범위 : 정렬 후, 첫번째 마지막번째
ans4 = nums[-1]-nums[0]

#출력
print(ans1)
print(ans2)
print(ans3)
print(ans4)
