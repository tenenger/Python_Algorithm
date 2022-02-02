def star(n, idx):
    if n == 1:
        board[idx][idx] = '*'
        return
    border = 4*(n-1) + 1

    for i in range(idx, border + idx):
        board[idx][i] = '*'
        board[idx+border-1][i] = '*'

        board[i][idx] = '*'
        board[i][idx+border-1] = '*'

    return star(n-1, idx+2)


n = int(input())
border = 4*(n-1) + 1
board = [[' ']*border for _ in range(border)]
idx = 0

star(n, idx)

for i in board:
    print(''.join(i))
