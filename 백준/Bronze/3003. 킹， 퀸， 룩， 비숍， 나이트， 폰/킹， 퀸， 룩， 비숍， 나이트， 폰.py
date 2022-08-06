#킹, 퀸, 룩, 비숍, 나이트, 폰
input_list = list(map(int, input().split()))
answer_list = [1, 1, 2, 2, 2, 8]

need_list = [il-a for a, il in zip(input_list, answer_list)]
print(*need_list)