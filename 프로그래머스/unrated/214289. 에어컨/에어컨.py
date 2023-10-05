'''
1. 문제이해
- 희망온도
- 전원이 켜져있는 동안 원하는 값으로 변경 가능
- 실내온도 != 희망온도 => 희망온도 방향으로 1도 상승 혹은 하강

- 실내온도 == 희망온다 => 실내온도 변하지 않음
- 실내온도 == 실외온도 => 실내온도 변하지 않음 

- 소비전력
    - 희망온도 != 실내온도 전력 a만큼
    - 희망온도 == 실내온도 전력 b만큼
    
- 차내 승객이 탑승 중일때는 항상 t1~t2 사이 유지
- 소비전력 최소화 

- 희망온도는 내가 정한다.


2. 접근방법
- 현재온도가 범위내에 있는지 판단
    - 범위내에 있으면 안켜도 된다 
- 모르겠음

3. 문제이해 참고
- 2차원 dp로 푼다.
    - i가 시간
    - j가 온도
    - value는 전력량
- 설정온도는 중요하지 않다.

4. 모르겠다
'''
def solution(temperature, t1, t2, a, b, onboard):
    k = 1000 * 100
    t1 += 10
    t2 += 10
    temperature += 10
    
    # DP[i][j] : i분에 j 온도를 만들 수 있는 가장 적은 전력
    DP = [[k] * 51 for _ in range(len(onboard))] # j = 0 : -10 // = 50 : 40
    DP[0][temperature] = 0
    
    flag = 1 # 에어컨을 가동했을때 온도가 변하는 방향
    if temperature > t2 :
        flag = -1

    for i in range(1, len(onboard)):
        for j in range(51):
            # 점화식
            arr = [k]
            if (onboard[i] == 1 and t1 <= j <= t2) or onboard[i] == 0:
                # 에어컨 끈 경우
                # 1. 에어컨을 키지 않고 실외온도와 달라서 실내온도가 -flag 되는 경우
                if 0 <= j+flag <= 50 :
                    arr.append(DP[i-1][j+flag])
                # 2. 에어컨을 키지 않고 현재온도 j 가 실외온도랑 같아서 변하지 않는 경우
                if j == temperature:
                    arr.append(DP[i-1][j])
                    
                # 에어컨 킨 경우
                # 3. 에어컨을 키고 현재온도가 변하는 경우
                if 0 <= j-flag <= 50:
                    arr.append(DP[i-1][j-flag] + a)
                # 4. 에어컨을 키고 현재온도가 희망온도라서 온도가 변하지 않는경우
                if t1 <= j <= t2:
                    arr.append(DP[i-1][j] + b)

                DP[i][j] = min(arr)
            
    answer = min(DP[len(onboard)-1]) # 마지막 시간대에서의 최소 전력량 
    return answer