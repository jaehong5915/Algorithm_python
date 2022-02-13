graph=[
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7] 
]
visited=[False]*9
def dsf(graph,v,visited):
    visited[v] = True
    # print(v, end=' ')    
    for i in graph[v]:
        print('v:::',v,'i:::',i)
        if not visited[i]:
            dsf(graph,i,visited)

dsf(graph,1,visited)