N,M = map(int, input().split())

def dfs(N,M,arr=[]): #dfs
    if len(arr) == M: 
        print(' '.join(map(str, arr))) 
        return 
    
    for i in range(1,N+1): 
        arr.append(i) 
        dfs(N,M) 
        arr.pop() 
        
dfs(N,M)