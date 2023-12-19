N = int(input())
result = -1
num = 0

while (num*5 <= N):
    if (N-num*5)%3 == 0:
        result = num+(N-num*5)//3
    num+=1
    
print(result)