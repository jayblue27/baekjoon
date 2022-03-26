# input
#1. n개의 숫자 
a = int(input())
#2. 공백없는 숫자 (n자리수) str로 받아서
b = input()

tmp = []
for i in range(a):    
    tmp.append(int(b[i])) #자리수별로 int변환 후 list에 투입

print(sum(tmp))     # 리스트 합 계산