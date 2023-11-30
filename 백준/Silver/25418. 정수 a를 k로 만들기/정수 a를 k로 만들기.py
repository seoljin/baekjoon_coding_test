A, k = map(int,input().split())

cnt = 0

while A != k:
    if k%2 == 0 and k >= A*2:
        k = k//2
    else:
        k -= 1
    cnt += 1

print(cnt)