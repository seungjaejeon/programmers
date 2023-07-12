# 문제 설명
# 주어진 항공권을 모두 이용하여 여행경로를 짜려고 합니다. 항상 "ICN" 공항에서 출발합니다.

# 항공권 정보가 담긴 2차원 배열 tickets가 매개변수로 주어질 때, 방문하는 공항 경로를 배열에 담아 return 하도록 solution 함수를 작성해주세요.

# 제한사항
# 모든 공항은 알파벳 대문자 3글자로 이루어집니다.
# 주어진 공항 수는 3개 이상 10,000개 이하입니다.
# tickets의 각 행 [a, b]는 a 공항에서 b 공항으로 가는 항공권이 있다는 의미입니다.
# 주어진 항공권은 모두 사용해야 합니다.
# 만일 가능한 경로가 2개 이상일 경우 알파벳 순서가 앞서는 경로를 return 합니다.
# 모든 도시를 방문할 수 없는 경우는 주어지지 않습니다.
def solution(tickets):
    answer = ["ICN"]
    visited = [False for _ in range(len(tickets))]
    tickets = sorted(tickets, key=lambda x : x[1])
    def dfs(tickets,begin_index, visited):
        nonlocal result
        if len(answer) == len(tickets)+1:
            result.append(list(answer))
            return
        else:
            for i in range(len(tickets)):
                if tickets[i][0]==tickets[begin_index][1] and visited[i]==False:
                    visited[i] = True
                    answer.append(tickets[i][1])
                    dfs(tickets, i, visited)
                    visited[i] = False
                    answer.pop()

    for i in range(len(tickets)):
        if tickets[i][0]=="ICN":
            begin_index = i
            break
    visited[begin_index] = True
    answer.append(tickets[begin_index][1])
    result = []
    dfs(tickets,begin_index, visited)
    return result[0]

tickets	=[["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
print(solution(tickets))
print(solution([["ICN", "BOO"], ["ICN", "COO"], ["COO", "DOO"], ["DOO", "COO"], ["BOO", "DOO"], ["DOO", "BOO"], ["BOO", "ICN"], ["COO", "BOO"]]))
print(solution([["ICN", "BBB"],["ICN", "CCC"],["BBB", "CCC"],["CCC", "BBB"],["CCC", "ICN"]]))
#["ICN", "BOO", "DOO", "BOO", "ICN", "COO", "DOO", "COO", "BOO"]