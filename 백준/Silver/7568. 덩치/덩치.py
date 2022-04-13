#입력1
num_student = int(input())

#입력2
student_list = []
for _ in range(num_student):
    weight, height = map(int, input().split())
    student_list.append((weight, height))

#계산 및 출력
for i in student_list: # 본인
    rank = 1    
    for j in student_list: # 비교대상
        # 몸무게, 키 둘다 자기보다 큰 사람 있으면
        if i[0] < j[0] and i[1] < j[1]:
                # 1등씩 올린다.
                rank += 1
    print(rank, end = " ")