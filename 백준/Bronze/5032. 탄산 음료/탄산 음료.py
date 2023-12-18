e,f,c = map(int,input().split())
answer = 0
num = e+f

while True:
    answer += num//c
    num = num//c + num % c
    if num < c:
        break

print(answer)