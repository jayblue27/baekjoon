'''
가격이 떨어지지 않은 기간은 몇 초인지 return
[1,2,3,2,3] -> [4,3,1,1,0]

처음부터 마지막 원소를 제외한 원소 순환
+1 초 씩 더해가고
만약j 값이 i보다 작을 경우 break

answer 리스트에 append

'''
def solution(prices):
    answer = []
    
    for i in range(len(prices)):
        tmp = prices[i]
        tmp_score = 0
        for j in range(i+1, len(prices)):
            tmp_score += 1
            if tmp > prices[j]:
                break
            
        answer.append(tmp_score)
    
    return answer