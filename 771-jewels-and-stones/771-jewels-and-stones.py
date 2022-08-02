class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        '''
        문제 이해가 어렵다. 
        책보고 푼다. 
        '''
        # 풀이 1 - 해시테이블 이용한 풀이 
        freqs = {}
        count = 0
        
        # 돌(stones)의 빈도 계산
        for stone in stones:
            if stone not in freqs:
                freqs[stone] = 1
            else:
                freqs[stone] += 1
        
        # 보석(J)의 빈도 합산
        for jewel in jewels:
            if jewel in freqs:
                count += freqs[jewel]
                
        return count
    
        