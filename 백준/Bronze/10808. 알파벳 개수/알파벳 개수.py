import sys
text = sys.stdin.readline().rstrip()
result_lst = [0]*(26)

for word in text :
    result_lst[ord(word)-97] += 1

for i in range(len(result_lst)) :
    print(result_lst[i],end=" ")