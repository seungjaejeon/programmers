from collections import deque
def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    pan = [[0 for i in range(102)] for j in range(102)]
    visited = [[0 for i in range(102)] for j in range(102)]
    for val in rectangle:
        for i in range(val[0]*2, val[2]*2+1):
            for j in range(val[1]*2, val[3]*2+1):
                pan[j][i] = 1
    for val in rectangle:
        for i in range(val[0]*2+1, val[2]*2):
            for j in range(val[1]*2+1, val[3]*2):
                pan[j][i] = 0 
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    def bfs(x,y):
        visited[x][y] = 1
        q = deque()
        q.append((x,y))
        while q:
            a, b = q.popleft()
            for i in range(4):
                nx = a + dx[i]
                ny = b + dy[i]
                if nx<0 or ny<0 or nx>=101 or ny>=101:
                    continue
                if visited[nx][ny]==0 and pan[nx][ny]:
                    visited[nx][ny]=1
                    pan[nx][ny] += pan[a][b]
                    q.append((nx,ny))
    
    bfs(characterX*2, characterY*2)
    answer = pan[itemX*2][itemY*2]
    for i in range(30):
        for j in range(30):
            print(pan[i][j], end=" ")
        print()
    
    return answer