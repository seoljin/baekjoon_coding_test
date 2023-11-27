N,M = map(int,input().split())
J = int(input())

count = 0
left = 1
right = M
location = []

for i in range(J):
    location.append(int(input()))
    if location[i] < left:
        count += left - location[i]
        right -= left - location[i]
        left = location[i]
    elif location[i] > right:
        count += location[i] - right
        left += location[i] - right
        right = location[i]

print(count)