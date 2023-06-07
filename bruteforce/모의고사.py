def solution(answers):
    answer = []
    count = [0,0,0]
    math1 = []
    math2 = []
    math3 = []
    math2_example = [2,1,2,3,2,4,2,5]
    math3_example = [3,3,1,1,2,2,4,4,5,5]
    for i in range(len(answers)):
        math1.append((i%5)+1)
        math2.append(math2_example[(i%8)])
        math3.append(math3_example[(i%10)])
    
    for i in range(len(answers)):
        if math1[i] == answers[i]:
            count[0]+=1
        if math2[i] == answers[i]:
            count[1]+=1
        if math3[i] == answers[i]:
            count[2]+=1
    max_val = max(count)
    for i in range(3):
        if count[i]==max_val:
            answer.append(i+1)
    return answer

# 수포자는 수학을 포기한 사람의 준말입니다. 수포자 삼인방은 모의고사에 수학 문제를 전부 찍으려 합니다. 
# 수포자는 1번 문제부터 마지막 문제까지 다음과 같이 찍습니다.

# 1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
# 2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
# 3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...

# 1번 문제부터 마지막 문제까지의 정답이 순서대로 들은 배열 answers가 주어졌을 때, 
# 가장 많은 문제를 맞힌 사람이 누구인지 배열에 담아 return 하도록 solution 함수를 작성해주세요.

# 제한 조건
# 시험은 최대 10,000 문제로 구성되어있습니다.
# 문제의 정답은 1, 2, 3, 4, 5중 하나입니다.
# 가장 높은 점수를 받은 사람이 여럿일 경우, return하는 값을 오름차순 정렬해주세요.