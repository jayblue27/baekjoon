# 백준 - 이상한 기호
'''
A@B -> (A+B)x(A-B)
'''

def ab_test(A,B):
    return (A+B)*(A-B)

A, B = map(int,input().split())
print(ab_test(A,B))