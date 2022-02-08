# 음료수 얼려 먹기
# 특정 지점 주변 상, 하, 좌, 우 살펴본 뒤 값이 '0' 이면서 아직 방문하지 않은 지점 방문
# 방문한 지점에서 다시 상, 하, 좌, 우 -> 방문 : 연결된 모든 지점 방문

# 1. n,m 받아서 for 문을 통해 grpah list 생성하기
# 2. 특정 노드를 방문한 뒤 연결된 모든 노드 방문하는 재귀함수 생성
# 2-1. 재귀함수 (1. 범위 벗어나면 종료 2. 현재 노드 방문 안했다면 방문 ==1 3. 상하좌우 재귀 호출 )
# 3. 모든 노드 방문 for m , for n -> cnt +=1 (생성 아이스크림)
n,m = map(int,input().split())
graph = []
for i in range(n):
    graph.append(list(map(int,input())))

def dfs(x,y):
    if x <= -1 or x >=n or y <= -1 or y >= m:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True        
    return False

cnt = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            print("생성")
            cnt += 1
print(cnt)