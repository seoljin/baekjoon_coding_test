N = int(input())
viewers = input()

cnt_c = viewers.count("LL")
cnt_s = viewers.count("S")

# 1 --> 2  2명 중 2
# 2 --> 3  4명 중 3
# 3 --> 4  6명 중 4
# 4 --> 5  8명 중 5
# ( 2*커플 수 - 커플수-1 ) + s개수

# answer = cnt_c-1+cnt_s

if cnt_c <= 1:
  answer = cnt_s + cnt_c*2
else:
  answer = cnt_c+1+cnt_s

print(answer)