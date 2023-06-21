import sys
input=sys.stdin.readline

def cal_dist(loc, distance) :
    if loc==1 : 
        return distance
    elif loc==4 :
        return w+distance
    elif loc==2 :
        return w+h+w-distance
    elif loc==3 :
        return w+h+w+h-distance

w, h = map(int,input().split())
num=int(input())

locations=[0]*(num+1)

dist=[]
for i in range(num+1) :
    loc, distance=map(int, input().split())
    dist.append(cal_dist(loc, distance))

dong_dist=dist[-1]

answer=0
for i in range(num):
    cal_distance=abs(dist[i]-dong_dist)

    total=2*(w+h)
    answer+=min(cal_distance,total-cal_distance)

print(answer)