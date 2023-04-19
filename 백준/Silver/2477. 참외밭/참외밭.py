s = []
x = []
y = []
lownum = []
 
k = int(input())
 
for i in range(6):
    way,dist = map(int,input().split()) 
    s.append([way,dist])
    if s[i][0] == 3 or s[i][0] == 4: 
        x.append(s[i][1])
    if s[i][0] == 1 or s[i][0] == 2: 
        y.append(s[i][1])
 
for i in range(6):
    if s[i][0] == s[(i+2)%6][0]:
        lownum.append(s[(i+1)%6][1])
        
print( ((max(x)*max(y)) - (lownum[0]*lownum[1])) * k )
