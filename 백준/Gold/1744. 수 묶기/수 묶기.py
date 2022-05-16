import sys
input = sys.stdin.readline

N = int(input())
lst_pos  = [] # 양수
lst_neg = [] # 음수
ans = 0

for _ in range(N):
  n = int(input())
  
  if n > 1:
    lst_pos.append(n)
  elif n == 1:
    ans += 1 # 1, 양수의 규칙에 의해 1을 더한다.
  else:
    lst_neg.append(n)

lst_pos.sort(reverse=True) # 양수의 큰 수부터 정렬한다.
lst_neg.sort() # 음수의 작은 수부터 정렬한다.

# 양수
# 짝수길이는 곱
# 남은건 덧셈
if len(lst_pos) % 2 == 0: # 양수가 짝수개 일경우 두개씩 곱해준다.
  for i in range(0, len(lst_pos), 2):
    ans += lst_pos[i] * lst_pos[i+1]
else:
  for i in range(0, len(lst_pos)-1, 2): 
    ans += lst_pos[i] * lst_pos[i+1]
  ans += lst_pos[len(lst_pos)-1] # 마지막 수는 더해준다.

# 음수 
# 짝수는 곱
if len(lst_neg) % 2 == 0: 
  for i in range(0, len(lst_neg), 2):
    ans += lst_neg[i] * lst_neg[i+1]
# 남은건 덧셈
else:
  for i in range(0, len(lst_neg)-1, 2):
    ans += lst_neg[i] * lst_neg[i+1]
  ans += lst_neg[len(lst_neg)-1] 

print(ans)