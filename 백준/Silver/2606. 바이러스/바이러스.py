#컴퓨터의 개수
n = int(input())
# 간선의 수
node = int(input())
# 연결된 곳을 받을 리스트
graph=[[] for _ in range(n+1)]
# 컴퓨터 방문 여부 확인
visited = [0]*(n+1)

# 열결된 간선의 정보
for i in range(node):
  a,b = map(int, input().split())
  graph[a] += [b] # 각 정점에 간선 정보 넣기 (방향X)
  graph[b] += [a]
  # print(graph) -> [[], [2, 5], [1, 3, 5], [2], [7], [1, 2, 6], [5], [4]]
    
def dfs(ans):
  # 방문한 곳 1
  visited[ans] = 1
  for j in graph[ans]:
    # 방문하지 않은 곳 0
    if visited[j] == 0:
      # 방문하지 않았으면 방문하고 1넣어주고 다시 탐색
      dfs(j)

dfs(1)

print(sum(visited)-1) # print(sum(visited))만 했다가 틀림