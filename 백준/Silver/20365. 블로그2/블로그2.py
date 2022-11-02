# 백준 - 블로그2 실버3
'''
1. 파란색, 빨간색 수 구한다.
2. 많은수를 한번에 칠한다 (1)
3. 적은수를 개별로 더한다.
-> 최소 작업수가 된다. 

*놓친부분
모든 R B를 count할게 아니라
연속되는건 하나의 문자로 봐야한다.
'''
from collections import defaultdict


N = int(input())
s = input().rstrip()
cnt = {'B': 0,'R': 0}
cnt[s[0]] += 1
for i in range(1,N):
    if s[i] != s[i-1]:
        cnt[s[i]] += 1

print(min(cnt['B'],cnt['R'])+1)