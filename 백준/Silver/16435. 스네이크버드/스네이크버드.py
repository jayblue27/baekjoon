import sys
input = sys.stdin.readline

n, l = map(int, input().split())
h = list(map(int, input().split()))

h.sort()
for fruit in h:
    if fruit <= l:
        l+=1
print(l)        
