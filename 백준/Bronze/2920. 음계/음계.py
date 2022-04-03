note = list( map(int, input().split() ) )

ascending = list(range(1,9))
descending = list(range(8,0,-1))

if note == ascending:
    print('ascending')
elif note == descending:
    print('descending')
else:
    print('mixed')