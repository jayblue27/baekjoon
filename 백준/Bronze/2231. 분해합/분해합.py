#입력
n = input()

# 분해합 만들기 함수
def gen_making(n):
    lst = [int(n)]
    for i in range(len(n)):
        lst.append(int(n[i]))
    
    return sum(lst)

# 숫자 순회 입력 숫자 까지
for i in range(int(n)):
    # 분해합 결과가 입력값이랑 같으면 출력하고 종료
    # 0부터 올라오는거니까 가장 작은 숫자가 출력 됨 
    if gen_making(str(i)) == int(n):
        print(i)
        break
#없으면 0 출력
else:
    print(0)