# 백준 - 최소공배수, 최대 공약수 
a, b = map(int, input().split())

#최대공약수
for i in range(max(a,b),0,-1):    
    if a%i ==0 and b%i ==0:
        print(i)
        break
#최소공배수
for i in range(min(a,b),a*b+1):
    if i%a == 0 and i%b ==0:
        print(i)
        break