A,B,C = map(int, input().split())
s = int(input())

C = C+s
B = B + (C // 60)
C = C%60
A = A + (B // 60)
B = B%60
A = A%24

print(A,B,C)