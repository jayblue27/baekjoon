n = int(input())
word = input()

def hash(num, word):
    ans = 0
    for i in range(num):
        tmp = (ord(word[i])-96) * (31**i)    
        ans += tmp
    print(ans%1234567891) # mod M (M : 1234567891 ) 

hash(n, word)