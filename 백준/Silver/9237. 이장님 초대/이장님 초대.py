N = int(input())
tree = list(map(int,input().split()))

tree = sorted(tree, reverse = True)
answer = 0

for i in range(1,N+1):
    answer = max(answer,tree[i-1]+i)

print(answer+1)