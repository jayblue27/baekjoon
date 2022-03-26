#알파벳 찾기
'''
string.find(찾을 문자)
find 메서드는 "찾을 문자" 혹은 "찾을 문자열"이 존재하는지 확인하고, 
찾는 문자가 존재 한다면 해당 위치의 index를 반환해주고
찾는 문자가 존재 하지 않는다면 -1 을 반환합니다.
만약에 찾는 문자나 문자열이 여러개 있다면 맨 처음 찾은 문자의 index를 반환하게 됩니다.
출처: https://blockdmask.tistory.com/569 [개발자 지망생]
'''

#input 소문자 단어 S
S = input()

#출력
#a가 처음등장하는 위치, b가 처음 등장하는 위치 , z까지 등장하는 위치 

for i in range(97,123):
    print(S.find(chr(i)), end=' ')
