import sys

n, m = map(int, sys.stdin.readline().split())
DNA = [list(map(str, sys.stdin.readline().strip())) for _ in range(n)]

res = ""
cnt = 0

# 반복문을 통해 서로 다른 4가지의 뉴클레오티드가 몇 개씩 있는지 확인
for i in range(m):
    DNAs = {"A": 0, "T": 0, "G": 0, "C": 0}

    for j in range(n):
        DNAs[DNA[j][i]] += 1

    # 뉴클레오티드 개수가 제일 많은게 Hamming Distance의 합이 가장 작은 DNA가 된다.
    # 사전순으로 정렬하기 위해 A/C/G/T 순으로 확인
    if max(DNAs["A"], DNAs["T"], DNAs["G"], DNAs["C"]) == DNAs["A"]:
        res += "A" # DNA
        cnt += DNAs["T"] + DNAs["G"] + DNAs["C"] # Hamming Distance

    elif max(DNAs["A"], DNAs["T"], DNAs["G"], DNAs["C"]) == DNAs["C"]:
        res += "C"
        cnt += DNAs["A"] + DNAs["T"] + DNAs["G"]

    elif max(DNAs["A"], DNAs["T"], DNAs["G"], DNAs["C"]) == DNAs["G"]:
        res += "G"
        cnt += DNAs["A"] + DNAs["T"] + DNAs["C"]

    elif max(DNAs["A"], DNAs["T"], DNAs["G"], DNAs["C"]) == DNAs["T"]:
        res += "T"
        cnt += DNAs["A"] + DNAs["G"] + DNAs["C"]


print(res)
print(cnt)