# 세점 받아서 사각형을 만들기위한 마지막 한점찾기
# 숫자 세개중에 갯수가 작은 값을 출력하면 되는데
# 규칙을 찾으면 조금 더 팬시하게 풀 수 있을 것 같다.
# 너무 어렵게 푼 느낌

# 입력값 받을 리스트 
lst_a = [] 
lst_b = []

# 입력
for _ in range(3):
    a, b = map(int, input().split())
    lst_a.append(a)
    lst_b.append(b)

# 결과 값 받을 리스트
lst = []
for i in range(3):
    # 예외처리 정사각형일 때  (정사각형은 직사각형이기도 하니까)
    if lst_a.count(lst_a[i]) == 3:
        lst.append(lst_a[i])
        break        
    # 그외경우 3점 중에 숫자가 1개만 있는 숫자를 결과 리스트에 넣는다.
    elif lst_a.count(lst_a[i]) == 1:
        lst.append(lst_a[i])    

    # b도 동일하게
for i in range(3):
    if lst_b.count(lst_b[i]) == 3:
        lst.append(lst_b[i])
        break
    elif lst_b.count(lst_b[i]) == 1:
        lst.append(lst_b[i])   
  
   
print(lst[0],lst[1])