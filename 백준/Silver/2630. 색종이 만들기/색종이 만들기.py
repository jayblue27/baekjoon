#백준 - 색종이 만들기 - 분할정복

#입력
N = int(input())
li = []
for i  in range(N):
    a=list(input().split())
    li.append(a)

#분할정복
def dv_paper(li):

    control = li[0][0] 
    case = control
    for x in range(0,len(li)):
        for y in range(0,len(li[0])):
            if li[x][y] != control:
                case = 2
                break
    if case ==2:
        mid = len(li) // 2

        p1 = []
        p2 = []
        p3 = []
        p4 = []

        for i in range(mid):    
            p1.append(li[i][0:mid])
            p2.append(li[i][mid:])

        for i in range(mid,len(li)):
            p3.append(li[i][0:mid]) 
            p4.append(li[i][mid:]) 

        return dv_paper(p1)+dv_paper(p2)+dv_paper(p3)+dv_paper(p4)
    else:
        return str(control)

# 출력
print(dv_paper(li).count('0'))
print(dv_paper(li).count('1'))