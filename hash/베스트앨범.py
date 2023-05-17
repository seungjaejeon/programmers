def solution(genres, plays):
    answer = []
    dic = {} # genre : plays 리스트를 가지는 딕셔너리
    index = {} # index : play 딕셔너리
    name = {}
    sum_genre = []
    for i in range(len(genres)):#dic, name, index dictionary initialize
        if genres[i] in dic:
            dic[genres[i]].append(plays[i])
            name[genres[i]] += plays[i]
        else: 
            dic[genres[i]] = [plays[i]]
            name[genres[i]] = plays[i]
        index[i] = plays[i]
        
    # 정렬을 통해 어떤 장르가 먼저 출력되어야 하는가를 판단하고자 함
    for i in dic:
        dic[i].sort()
        sum_genre.append(sum(dic[i]))
    sum_genre.sort()

    for i in range(len(sum_genre)-1, -1, -1):
        for j in dic:
            if sum_genre[i] == name[j]: # 정렬된 합 뒤에서부터 찾기
                if len(dic[j])>=2: # 장르별 곡이 두개 이상일 경우
                    for k in range(len(dic[j])-1,len(dic[j])-3,-1):
                        for t in index:
                            if dic[j][k] ==index[t]: # dic[j]에서 index[t]와 같은 => index
                                if t not in answer:#play수가 같을때 두번 출력됨을 방지
                                    answer.append(t)
                else: # 장르별 곡이 하나일경우
                    for t in index:
                            if dic[j][0] ==index[t]:
                                if t not in answer:#play수가 같을때 두번 출력됨을 방지
                                    answer.append(t)
                                
    return answer


# 스트리밍 사이트에서 장르 별로 가장 많이 재생된 노래를 두 개씩 모아 베스트 앨범을 출시하려 합니다. 
# 노래는 고유 번호로 구분하며, 노래를 수록하는 기준은 다음과 같습니다.

# 속한 노래가 많이 재생된 장르를 먼저 수록합니다.
# 장르 내에서 많이 재생된 노래를 먼저 수록합니다.
# 장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록합니다.
# 노래의 장르를 나타내는 문자열 배열 genres와 노래별 재생 횟수를 나타내는 정수 배열 plays가 주어질 때, 
# 베스트 앨범에 들어갈 노래의 고유 번호를 순서대로 return 하도록 solution 함수를 완성하세요.


# 제한사항
# genres[i]는 고유번호가 i인 노래의 장르입니다.
# plays[i]는 고유번호가 i인 노래가 재생된 횟수입니다.
# genres와 plays의 길이는 같으며, 이는 1 이상 10,000 이하입니다.
# 장르 종류는 100개 미만입니다.
# 장르에 속한 곡이 하나라면, 하나의 곡만 선택합니다.
# 모든 장르는 재생된 횟수가 다릅니다.