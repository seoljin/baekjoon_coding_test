N = int(input())

arr = [0]*1002
arr[1] = 1
arr[2] = 1

#  피보나치 형태 f(n) = f(n-1) + f(n-2) (n>=3) (f(1) = 1, f(2) = 1)
for i in range(3, N+2):
    arr[i] = arr[i-1] + arr[i-2]


print(arr[N+1]%10007)