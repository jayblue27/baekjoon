#백준 - 나는야 포켓몬 마스터 이다솜 
'''
이름 들어오면 번호
번호 들어오면 이름
'''
import sys
input = sys.stdin.readline

#입력 1<= N, M <= 100,000
# N : 포켓몬 개수
# M : 문제의 개수
N,M = map(int, input().split())
# 포켓몬 이름 입력
pokemons_num = {}
pokemons_text = {}

for i in range(1, N+1):
    tmp = input().strip()
    pokemons_num[i] = tmp
    pokemons_text[tmp] = i

# 문제 입력
for _ in range(M):
    tmp = input().strip()
    if tmp.isalpha():
        print(pokemons_text[tmp])
    else:
        print(pokemons_num[int(tmp)])