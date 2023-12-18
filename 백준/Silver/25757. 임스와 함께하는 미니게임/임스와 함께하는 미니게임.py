N, kind = input().split()
N = int(N)

game = set()

for i in range(N):
    game.add(input())
    
answer = 0

for i in game:
    if kind == 'Y':
        answer = len(game)
    elif kind == 'F':
        answer = len(game)// 2
    else:
        answer = len(game) // 3

print(answer)