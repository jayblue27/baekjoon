score = []
for _ in range(5):
    a = int(input())
    if a < 40:
        a = 40
    score.append(a)

print(int(sum(score)/5))