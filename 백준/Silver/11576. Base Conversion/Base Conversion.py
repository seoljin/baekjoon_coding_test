A, B= map(int, input().split())
m = int(input())
num = list(map(int,input().split()))
num.reverse()

# A진수를 10진수 만들기
deci = 0
for i in range(m):
    deci += num[i]*(A ** i)

#print(deci)

# 10진수를 B진수로 만들기
#reverse_B = ''
#result = ''

#while deci > 0:
#    deci, mod = divmod(deci, B)
#    reverse_B += str(mod)

# print(reverse_B[::-1])

# result = reverse_B[::-1]

# 10진수를 B진수로 만들기
b = []
while deci > 0:
    b.append(deci%B)
    deci //= B

b.reverse()
#print(result)
for i in range(len(b)):
    print(b[i], end= ' ')