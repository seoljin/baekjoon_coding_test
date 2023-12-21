T = int(input())

for _ in range(T):
    J, N = map(int, input().split())
    arr = []
    for _ in range(N):
        R, C = map(int, input().split())
        arr.append(R*C)

    arr.sort(reverse=True)

    answer = 0
    i = 0
    while J>0:
        J -= arr[i]
        answer += 1
        i += 1

    print(answer)