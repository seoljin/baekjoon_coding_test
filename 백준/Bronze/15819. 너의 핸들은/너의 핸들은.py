N, I = map(int,input().split())
arr = []
for i in range(N):
    arr.append(input())

arr.sort()

print(arr[I-1])