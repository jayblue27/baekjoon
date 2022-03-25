# 숫자 10개 입력 
# set함수 사용 
# set 함수 중복 제거 해준다.

tmp = []        # 임시 리스트

for i in range(10): 
    num = int(input())  # int 값 입력
    num_ = num%42        # 42로 나눈 나머지
    tmp.append(num_)     # 리스트에 추가

tmp =set(tmp)           # 중복값 제거89
print(len(tmp))                # 길이 출력

#나머지가 서로 다른 값의 갯수 를 구하는 문제