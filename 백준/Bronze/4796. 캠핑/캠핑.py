i=1
while True:                                 
    L,P,V = map(int, input().split())                   # L,P,V 인풋 받기
    if L == 0 and P == 0 and V == 0:                    # L,P,V 값에 모두 0이 들어오면 종료
        break
    else:
        print(f'Case {i}: {V//P*L + min(V%P, L)}')      # 출력
        i+=1   