# 수열 생성 함수
def sequence_maker(num):        
    # 각 자리수 생성
    만 = num // 10000
    천 = (num - (num // 10000 * 10000)) // 1000
    백 = (num - (num // 1000 * 1000)) // 100
    십 = (num - (num // 100 * 100)) // 10
    일 = num % 10
    
    # 수열 생성 부분
    if num < 10:
        return num + 일
    elif num < 100:
        return num + 십 + 일
    elif num < 1000:
        return num + 백 + 십 + 일
    elif num < 10000:
        return num + 천 + 백 + 십 + 일
    else:
        return num + 만 + 천 + 백 + 십 + 일

# 10000까지의 수열 리스트 만들기
seq_list = [sequence_maker(i) for i in range(1,10001)]        

# 수열 list에 없으면(셀프넘버이면) 출력
for i in range(1,10001):
    if i not in seq_list:
        print(i)