def solution(n):
    ans = []
    for i in str(n)[::-1]:
        ans.append(int(i))
    
    return ans
