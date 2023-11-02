N, B = map(str, input().split())       # 수 입력

num = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ' # 숫자

B = int(B)
re_N = N[::-1]  # 입력받은 수 뒤집기
# print(re_N)   # 뒤집힌 수 확인

sum = 0                        # sum = 0 선언
for i,n in enumerate(re_N):    # enumerate 사용해서 인덱스랑 요소로 나눔
  sum += (num.index(n)*B**i)   # 해당 진법을 10진수로 바꾸는 작업

print(sum)                     # 결과 출력