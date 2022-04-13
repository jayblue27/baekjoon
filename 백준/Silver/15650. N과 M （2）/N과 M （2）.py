n, m = list(map(int,input().split()))
s = list()

def dfs(idx):    
    # 종료조건 
    # len의 원소가 4개 차면 출력
    if len(s)==m:
        # 원소를 공백으로 join후 출력
        print(' '.join(map(str,s)))        
        return
    
    # 1부터 4까지
    for i in range(idx,n+1):
        # 리스트(s)에 i가 없으면
        # 있으면 다음 i로 넘어간다.

        if i not in s:
            # 리스트에 원소 추가 하고
            s.append(i)            
            # 재귀 (시작 idx를 1개씩 올린다.)
            dfs(i+1)
            # 리스트서 맨마지막꺼 제거
            s.pop()
            
dfs(1)