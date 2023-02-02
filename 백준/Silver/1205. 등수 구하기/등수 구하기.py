n, score, p = map(int, input().split())
board = []
if n != 0:
    board = list(map(int, input().split()))
    board.append(score)
    board.sort(reverse=True)
    rank = board.index(score) + 1
    if rank > p:
        print(-1)
    else:
        if score == board[-1] and n == p:
            print(-1)
        else:
            print(rank)
else:
    print(1)