import copy

Eratos = [0]*10000
Eratos[0] = 0
Eratos[1] = 1
for i in range(2,100):
    if Eratos[i]==0:
        temp = i+i
        while temp<10000:
            Eratos[temp]=1
            temp=temp+i
            
from collections import deque
def solution(start,goal):
    queue = deque()
    queue.append((start,0))
    visitied = list()
    visitied.append(start)
    while queue:
        nownum, count = queue.popleft()
        if nownum == goal:
            return count
        for i in range(4):
            for j in range(10):
                newnum = list(copy.deepcopy(str(nownum)))
                newnum[i]=str(j)
                if 999<int(''.join(newnum))<10000:
                    if Eratos[int(''.join(newnum))] == 0:
                        if int(''.join(newnum)) not in visitied:
                            queue.append((int(''.join(newnum)),count+1))
                            visitied.append(int(''.join(newnum)))
    return "Impossible"
def main():
    for test_case in range(int(input())):
        start, goal = map(int,input().split())
        print(solution(start,goal))

main()