word=input()
bomb=input()
stack=[]

for i in word:
    stack.append(i)
    if stack and stack[-1]==bomb[-1]:
        if ''.join(stack[-len(bomb):])==bomb:
            del stack[-len(bomb):]
if stack:
    for p in stack:
        print(p, end='')
else:
    print("FRULA")