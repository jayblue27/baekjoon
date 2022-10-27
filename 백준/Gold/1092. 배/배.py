#백준 - 배 
'''
N개의 크레인 <= 50
M개의 박스   <= 10000

1분에 박스 하나씩

모든 박스를 배로 옮기는데 드는 시간의 최소값 
만약 모든박스를 배로 옮길 수 없으면 -1
  -> 박스 용량이 크레인 용량보다 크면 

'''
import sys
input = sys.stdin.readline
N=int(input())
cranes = list(map(int,input().split()))
cranes.sort(reverse=True)

M=int(input())
boxes = list(map(int,input().split()))
boxes.sort(reverse=True)


max_crane = max(cranes)
max_box = max(boxes)

cnt=0

# 예외처리
if max_box > max_crane:
    print(-1)
# 그외
else:
    while len(boxes)>0:        
        for crane in cranes:
            for box in boxes:
                if crane >= box:
                    boxes.remove(box)
                    break                    
        cnt += 1
    print(cnt)
