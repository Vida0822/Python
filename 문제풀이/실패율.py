def solution(N, stages):
    answer = [] 
    length = len(stages) 

    # 스테이지 번호를 1부터 N까지 증가시키며 
    for i in range(1, N+1):

        # 해당 스테이지에 머물러 있는 사람수 계산
        count = stages.count(i)

        # 실패율 계산
        if length == 0 :
            fail = 0 
        else : 
            fail = count / length 
        # 이 경우 멈춘사람이 없으면 count가 0이라 실패율이 0이 되고, 
        # 더 이상 검사할 플레이어가 없으면 남은 검사 스테이지들은 자동으로 실패율이 0이된다 

        # 리스트에 튜플(스테이지 번호, 실패율) 원소 삽입한다
        answer.append((i,fail)) 

        # 전체 플레이어의 수에서 현재 스테이지에 머무르고 있는 플레이어의 수를 뺍니다. 
        length -= count 
    
    # 실패율 기준으로 스테이지 내림차순 정렬 
        answer = sorted(answer, key = lambda t: t[1], reverse=True)

    # 배열 형태로 반환 
    answer = [i[0] # stage번호만 반환해 배열 생성 
              for i in answer] # 튜플값을 하나씩 꺼내서
    return answer 