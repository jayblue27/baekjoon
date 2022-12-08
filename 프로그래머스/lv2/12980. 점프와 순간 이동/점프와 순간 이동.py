'''
0부터 n까지 이동
- 점프하면 1칸에 에너지 1씩 소모
- 순간이동(현재까지 이동한 거리의 2배) 에너지 소모 없음 
'''

# # 시간초과
# def solution(n):
#     ans = 0
#     while n != 0:
#         print(n)
#         if n%2==0:
#             n //= 2
#         else: 
#             n-=1
#             ans+=1

#     return ans

# 참고
def solution(n):
    return bin(n).count('1')
