max_limit = 10000

def Goldbach():
    #에라토스테네스의 체 생성
    eratos_sieve = [False, False] + [True] * max_limit # 0,1 제외 전부 True   
    
    for i in range(2, int(max_limit**0.5)+1):  
        if eratos_sieve[i] == True:
            for j in range(i + i, max_limit+1, i):
                eratos_sieve[j] = False

    #테스트 케이스 수 입력
    T = int(input())
    for _ in range(T):
        #숫자 입력
        n = int(input())

        # 골드바흐 파티션이 여러 가지일 경우, 두 소수의 차이가 가장 작은 것을 출력해야하기 때문에 
        # 입력 값 A 의 절반부터 시작해서 소수가 아닐경우 A는 1씩 줄이고, B는 1씩 늘려 나가면서
        # 해당 케이스가 나타날 경우 반환
        A = n // 2
        B = A
        for _ in range(max_limit):
            if eratos_sieve[A] and eratos_sieve[B]:
                print(A, B)
                break
            A -= 1
            B += 1

Goldbach()