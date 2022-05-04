# 백준 - 덱 
from collections import deque
import sys

deque = deque()
N = int(input())
input = sys.stdin.readline

for i in range(N):
    command = input().split()

    if command[0] == "push_front":
        deque.appendleft(command[1])
    elif command[0] == "push_back":
        deque.append(command[1])
    elif command[0] == "pop_front":
        if deque:
            print(deque[0])    
            deque.popleft()
        else:
            print("-1")
    elif command[0] == "pop_back":
        if deque:
            print(deque[-1])    
            deque.pop()
        else:
            print("-1")
    elif command[0] == "size":
        print(len(deque))
    elif command[0] == "empty":
        if deque:
            print("0")
        else:
            print("1")
    elif command[0] == "front":
        if deque:
            print(deque[0])
        else:
            print("-1")
    elif command[0] == "back":
        if deque:
            print(deque[-1])
        else:
            print("-1")