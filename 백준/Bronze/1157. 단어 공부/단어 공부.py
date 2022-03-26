#단어중 가장 많이 쓰인 알파벳 출력, 
#가장 많이 쓰인 알파벳 숫자가 똑같으면 물음표 출력

#소문자로 문장 입력 받기
S = input().lower()

#임시 dict
tmp = {} # dict

#알파벳 소문자 a~z 아스키코드 (97~122까지 순환)
for i in range(97,123):
    count = S.count(chr(i)) # 해당 알파벳 몇개 포함 됐는지 확인
    tmp[chr(i)] = count     # 알파벳 key, count 수 = value 형태로 dict안에 값 저장

# value 값 기준으로 내림차순 정렬
reverse_tmp = sorted(tmp.items(),
                     reverse=True,
                     key=lambda item: item[1])

# vlaue값 기준 첫번째 값이랑 두번째 값이랑 동일하면 제일 많은 알파벳이 2개 이상이라고 보고 
# 물음표 출력
if reverse_tmp[0][1] == reverse_tmp[1][1]:
    print('?')
# 아니면 해당 알파벳 대문자로 변환해서 출력
else:
    print(reverse_tmp[0][0].upper())
