import sys

g = int(sys.stdin.readline().rstrip())

p = int(sys.stdin.readline().rstrip())

count = 0

plane_list = []
for i in range(p):
    plane_list.append(int(sys.stdin.readline().rstrip()))

#게이트는 처음 자기자신 값을 가짐 ex) g= 4 인 경우 [0, 1, 2, 3, 4]
gate_parent = [i for i in range(g+1)]


def find(plane):
    # 게이트가 자기 자신을 가르키는 경우 == 게이트가 비어있음
    if gate_parent[plane] == plane:
        return plane
    gate_parent[plane] = find(gate_parent[plane])
    return gate_parent[plane]

for plane in plane_list:
    temp = find(plane)
    if temp == 0:
        break
    gate_parent[temp] = gate_parent[temp-1]  #게이트가 채워졌으므로 옆의 게이트로 부모 게이트를 바꿔줌
    count += 1

print(count)