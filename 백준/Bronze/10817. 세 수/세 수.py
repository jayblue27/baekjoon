#백준 - 세수 
'''
정수 3개, 두번째로 큰 정수 출력
'''
a = list(map(int,input().split()))
a.sort()
print(a[1])