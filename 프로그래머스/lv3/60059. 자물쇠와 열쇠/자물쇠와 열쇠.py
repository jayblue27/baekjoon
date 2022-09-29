'''
열쇠 회전 가능
회전(4) * 이동(상하좌우 끝-1 까지)

4가지경우 - 0도, 90도, 180도, 270도

돌기끼리 만나면 안됨 -> 모든 값이 1이면 true 

'''

def turn_key(l, key):
    new_key = [item[:] for item in key]

    for i in range(l):
        for j in range(l):
            new_key[i][j] = key[l - (j + 1)][i]

    return new_key


def check(lock, lock_l):
    for i in range(lock_l):
        for j in range(lock_l):
            if lock[i + lock_l][j + lock_l] != 1:
                return False
    return True


def solution(key, lock):
    key_l = len(key)
    lock_l = len(lock)
    new_lock = [[0] * (lock_l * 3) for _ in range(lock_l * 3)]

    new_len = len(new_lock)

    for i in range(lock_l):
        for j in range(lock_l):
            new_lock[i + lock_l][j + lock_l] = lock[i][j]

    for i in range(4):
        key = turn_key(key_l, key)

        for i in range(new_len - key_l):
            for j in range(new_len - key_l):

                for k in range(key_l):
                    for p in range(key_l):
                        new_lock[i + k][j + p] += key[k][p]

                if check(new_lock, lock_l):
                    return True

                else:
                    for k in range(key_l):
                        for p in range(key_l):
                            new_lock[i + k][j + p] -= key[k][p]

    return False