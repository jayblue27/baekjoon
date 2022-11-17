'''
완전탐색으로 풀어야 겠다라는 생각까지는 했는데
* 표시가 포함된 banned_id를 어떻게 처리해야할지 몰라서 풀지를 못했다. 

참고함

'''

import re
from itertools import permutations
def solution(user_id, banned_id):
    ban = ' '.join(banned_id).replace('*','.')
    # print(ban)
    answer = set()
    for i in permutations(user_id, len(banned_id)):
        if re.fullmatch(ban, ' '.join(i)):
            # print(' '.join(i))
            answer.add(''.join(sorted(i)))
            
    return len(answer)