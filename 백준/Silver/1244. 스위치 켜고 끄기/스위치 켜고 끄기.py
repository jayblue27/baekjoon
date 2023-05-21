from sys import stdin

n = int(stdin.readline())
switch = [0] + list(map(int, stdin.readline().split()))

for i in range(int(stdin.readline())):
    g, num = map(int, stdin.readline().split())

    if g == 1:
        for i in range(num, n + 1, num):
            switch[i] = 1 if switch[i] == 0 else 0

    elif g == 2:
        if num + 1 > n or num - 1 < 1:
            switch[num] = 1 if switch[num] == 0 else 0
        else:
            if switch[num + 1] == switch[num - 1]:
                left = num - 1
                right = num + 1

                while 1:
                    if left - 1 < 1 or right + 1 > n:
                        break

                    if switch[left - 1] != switch[right + 1]:
                        break

                    else:
                        left -= 1
                        right += 1

                for i in range(left, right + 1):
                    switch[i] = 1 if switch[i] == 0 else 0
            else:
                switch[num] = 1 if switch[num] == 0 else 0


for i in range(1, n, 20):
    print(*switch[i:i+20])