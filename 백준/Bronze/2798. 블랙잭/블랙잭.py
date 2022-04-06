N, M = map(int, input().split())
cards = list(map(int, input().split()))

def black(num, target):
    # breakpoint()
    tmp_sum = 0
    for i in range(0,num):
        for j in range(i+1,num):
            for k in range(j+1,num):
                if tmp_sum > target:
                    continue
                elif tmp_sum <= sum([cards[i],cards[j],cards[k]]) < target+1 :
                    tmp_sum = sum([cards[i],cards[j],cards[k]])                    
    return tmp_sum

print(black(N,M))