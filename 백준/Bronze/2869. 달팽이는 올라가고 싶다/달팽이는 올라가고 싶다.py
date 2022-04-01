# %%time 소요시간 확인용
# 동작 시간이 0.25s로 고정되어 있는게 함정인 듯
# 반복문으로 푸니까 숫자가 커지니까 시간이 굉장히 많이 늘어남 O(n)

#올림 함수 사용을 위하여 math 불러옴
import math 

# 입력 
# A:상승, B:하락, V:정상높이
A,B,V = map(int, input().split())

# 정상에 도착하면 안떨어지니까
first_step = V - A  # 첫걸음에 정상(V)에 도착할 경우를 생각
gap = A - B # 남은 높이

#math.ceil() 올림
#남은 높이를 A-B의 차이 만큼 날짜가 걸리니까 나누는데
#남은 높이가 1이라도 있으면 하루가 더 걸린다고 봐야하니까 올림을 썼음
#+ 1부분은 first step에서 소비된 날짜 하루
print(math.ceil(first_step / gap)+1)
