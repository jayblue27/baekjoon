N = int(input())    
num = list(map(int, input().split()))  
current = [0] * N 
cnt = 0   
for i in range(N):
    if num[i] != current[i]:    
        cnt += 1
        current[i] = not current[i] 

        if i+1 < N:
            current[i+1] = not current[i+1]
        if i+2 < N:
            current[i+2] = not current[i+2]

print(cnt)