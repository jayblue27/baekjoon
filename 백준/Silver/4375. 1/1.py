import sys

arr = []
for i in range(10000):
  num = sys.stdin.readline()
  if num == '':
    break
  arr.append(int(num))

for num in arr:
  cnt = 1
  temp = 1
  while(True):
    if temp % num ==0: 
      print(cnt)
      break
    cnt+=1
    temp = temp*10 +1 