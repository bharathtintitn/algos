import sys

graph = {
    1: [2,3],
    2: [4,5],
    3: [6,7],
    4: [],
    5: [],
    6: [],
    7: []
  }


def bfs(graph,source):

  visited = []
  visited.append(source)
  
  while len(visited) > 0:
    node = visited.pop(0)
    reachable = graph[node]
    for i in reachable:
      print i,
      visited.append(i)

   

if __name__ == "__main__":

  bfs(graph,1)
