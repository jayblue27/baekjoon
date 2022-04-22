t = int(input())

a, b, c = 0, 0 ,0

a = t // 300
t = t - (300 * a)

b = t // 60
t = t - (60 * b)

c = t // 10
t = t - (10 * c)

if t > 0 :
    print(-1)
else:
    print(a,b,c)
