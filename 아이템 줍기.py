from collections import deque
def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    pan = [[-1 for i in range(102)] for j in range(102)]
    visited = [[1 for i in range(102)] for j in range(102)]
    for val in rectangle:
        for i in range(val[0]*2, val[2]*2+1):
            for j in range(val[1]*2, val[3]*2+1):
                if val[0]*2 < i < val[2]*2 and val[1]*2< j < val[3]*2:
                    pan[j][i] = 0
                elif pan[j][i]!=0:
                    pan[j][i] = 1
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    def bfs(x,y):
        q = deque()
        q.append((x,y))
        while q:
            a, b = q.popleft()
            for i in range(4):
                nx = a + dx[i]
                ny = b + dy[i]
                if nx<0 or ny<0 or nx>=101 or ny>=101:
                    continue
                if visited[nx][ny]==1 and pan[nx][ny]==1:
                    visited[nx][ny]+=visited[a][b]
                    q.append((nx,ny))
    
    bfs(characterY*2, characterX*2)
    answer = visited[itemY*2][itemX*2]//2
    
    return answer