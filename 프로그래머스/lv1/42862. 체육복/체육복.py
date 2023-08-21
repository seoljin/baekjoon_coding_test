def solution(n, lost, reserve):
    # 여벌 체육복이 있는데 도난 당한 학생을 제거하기 위해 집합에서 빼줌
    lost2=list(set(lost)-set(reserve)) 
    reserve2=list(set(reserve)-set(lost))
    # 순서대로 정렬
    reserve2.sort()
    lost2.sort()
    
    for i in reserve2:
        front=i-1
        back=i+1
        if front in lost2:       # 앞사람 확인
            lost2.remove(front)
        elif back in lost2:      # 뒷사람 확인
            lost2.remove(back)
        else:
            continue
            
    return n-len(lost2) # 여전히 잃어버린 사람 수를 전체에서 빼면 답