# 게임 맵의 상태 maps가 매개변수로 주어질 때, 
# 캐릭터가 상대 팀 진영에 도착하기 위해서 지나가야 하는 칸의 개수의 최솟값을 return 하도록 solution 함수를 완성해주세요. 
# 단, 상대 팀 진영에 도착할 수 없을 때는 -1을 return 해주세요.

# 제한사항
# maps는 n x m 크기의 게임 맵의 상태가 들어있는 2차원 배열로, n과 m은 각각 1 이상 100 이하의 자연수입니다.
# n과 m은 서로 같을 수도, 다를 수도 있지만, n과 m이 모두 1인 경우는 입력으로 주어지지 않습니다.
# maps는 0과 1로만 이루어져 있으며, 0은 벽이 있는 자리, 1은 벽이 없는 자리를 나타냅니다.
# 처음에 캐릭터는 게임 맵의 좌측 상단인 (1, 1) 위치에 있으며, 상대방 진영은 게임 맵의 우측 하단인 (n, m) 위치에 있습니다.

from collections import deque
def solution(maps):
    answer = 0
    n = len(maps)
    m = len(maps[0])
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def bfs(x,y):
        q = deque()
        q.append((x,y))

        while q:
            x, y = q.popleft()
            for i in range(4): #위 아래 우 좌 확인
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or ny < 0 or nx >= n or ny >= m:  #maps범위 벗어나는지 확인
                    continue
                if maps[nx][ny] == 0: #벽인지 확인
                    continue
                if maps[nx][ny] == 1: #통로일경우
                    maps[nx][ny] = maps[x][y] + 1 #길이 1 추가
                    q.append((nx, ny)) #그곳으로 이동
        return maps[n-1][m-1]

    if bfs(0,0) == 1: #그대로 1이면 도착못했다는 증거
        return -1
    else:
        answer = bfs(0,0)

    return answer
maps = [[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]
print(solution(maps))