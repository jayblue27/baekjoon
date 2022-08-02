class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        '''
        문제 이해가 어렵다. 
        책보고 푼다. 
        '''
#         # 풀이 1 - 해시테이블 이용한 풀이 
#         freqs = {}
#         count = 0
        
#         # 돌(stones)의 빈도 계산
#         for stone in stones:
#             if stone not in freqs:
#                 freqs[stone] = 1
#             else:
#                 freqs[stone] += 1
        
#         # 보석(J)의 빈도 합산
#         for jewel in jewels:
#             if jewel in freqs:
#                 count += freqs[jewel]
                
#         return count
    
#         # 풀이 2 - defaultdict 쓰면 if절 줄일 수 있음 
#         freqs = collections.defaultdict(int)
#         count = 0
        
#         # default dict라서 key값 없어도 바로 입력 가능
#         for s in stones:
#             freqs[s] += 1
            
#         for j in jewels:
#             count += freqs[j]
        
#         return count
    
#         # 풀이 3 - Counter로 for 하나 생략
#         freqs = collections.Counter(stones)
#         count = 0
        
#         for j in jewels:
#             count += freqs[j]
#         return count 
    
        # 풀이 4 - 파이썬풀이 - 오 쫌 파격적이다 리스트 없이도 이런식으로 컴프리헨션 처럼 표현이 가능하구나
        return sum(s in jewels for s in stones) # sum(True,True,True,False,False,False,False)
        