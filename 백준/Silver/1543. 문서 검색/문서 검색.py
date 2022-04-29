# 백준 - 문서 검색 
# 어떤 단어가 총 몇번 등장했는지 카운팅
# 중복은 제거

#문서
a = input()
#해당단어
b = input()


tmp = '' #문자열 담을 임시 변수
cnt = 0  #카운트 변수
for i in a: 
    tmp += i # 문서 순회하며 한자씩 입력 
    if b in tmp:  # b가 임시변수안에서 발견되면
        tmp = '' # tmp 초기화
        cnt += 1 # cnt 1 증가
print(cnt)