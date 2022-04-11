from collections import defaultdict

#입력
n = int(input())
lst = []
for i in range(n):
    lst.append(input())

#정렬
def sort(lst):    
    dic = defaultdict(set)
    for i in lst:
        dic[len(i)].add(i)
    #출력
    for i in sorted(dic.keys()):
        for j in sorted(dic[i]):
            print(j)
    
sort(lst)