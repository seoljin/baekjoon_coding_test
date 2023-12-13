N, M = map(int, input().split())

a = set() # 중복제거
for i in range(N):
    a.add(input())

b = set() # 중복제거
for i in range(M):
    b.add(input())
    
answer = list(a & b)  # &은 교집합
# answer

print(len(answer))

answer.sort() # 정렬
for i in answer:
    print(i)