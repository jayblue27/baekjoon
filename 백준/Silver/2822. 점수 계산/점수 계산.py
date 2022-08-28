score = []
quiz_num = 1
for _ in range(8):
    score.append([quiz_num, int(input())])
    quiz_num+=1

score.sort(key=lambda x : x[1], reverse=True)

nums = []

total = 0
for num, s in score[:5]:
    total += s
    nums.append(num)

print(total)

nums.sort()
print(*nums)