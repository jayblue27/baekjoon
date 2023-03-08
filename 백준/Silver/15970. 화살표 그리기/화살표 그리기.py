import sys
n = int(sys.stdin.readline())
arr = []
for i in range(n):
    [x,color] = map(int,sys.stdin.readline().split())
    arr.append([color,x])
sum = 0
arr.sort()

for i in range(n):
    if i==0 : 
        if arr[i][0]==arr[i+1][0]:
            sum = sum+(arr[i+1][1]-arr[i][1]) 
    elif i==n-1: 
        if arr[i-1][0]==arr[i][0]:
            sum = sum+(arr[i][1]-arr[i-1][1]) 
    else: 
        min = 9912341234
        if arr[i-1][0]==arr[i][0]: 
            min = arr[i][1]-arr[i-1][1] 
        if arr[i][0]==arr[i+1][0]: 
            sub = arr[i+1][1]-arr[i][1] 
            if sub<min: 
                min = sub 
        if min<9912341234: 
            sum = sum+min 
print(sum) 