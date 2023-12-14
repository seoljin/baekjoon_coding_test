T = int(input())

for _ in range(T):
    data = input().split()
    for i in data:
        print(i[::-1], end=' ')
    print()