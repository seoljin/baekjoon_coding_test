def solution(number, k):
    answer = ''
    comb = []
    for i in number:
        while k>0 and comb and comb[-1] < i:
            comb.pop()
            k -= 1
        comb.append(i)
        # print(comb)
        '''	['1']
            ['9']
            ['9', '2']
            ['9', '4']'''
    if k != 0:
        comb = comb[:-k]
        
    answer = ''.join(comb)

    return answer