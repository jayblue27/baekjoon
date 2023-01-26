n = int(input()) # 사람 수 입력
n_time = list(map(int,input().split())) # 각 사람이 돈을 인출하는데 걸리는 시간
n_time.sort() # 정렬 - sort 기본값은 오름차순 내림차순은 .sort(reverse=True)

result = 0 # 결과값 변수 선언

for i in range(1,n+1):  # 1부터 n+1번까지 반복, 
    result += sum(n_time[:i]) 
    #리스트 n_time[0]부터 [i-1] 까지의 합을 순차적으로 result에 더함
                                 
print(result) # 결과 출력