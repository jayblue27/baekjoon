#백준 - 폴리오미노

board = input() 
board = board.replace("XXXX", "AAAA").replace("XX", "BB")
if 'X' in board:
    print(-1)
else:
    print(board)