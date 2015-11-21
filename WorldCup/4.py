def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                queue.append((next, path + [next]))

n=int(raw_input().rstrip('\n'))
A=map(int ,raw_input().rstrip('\n').split(" "))
graph={}

for e in range(n):
    graph[str(e+1)]=set([])

for i in range(1,n):
    e=map(int ,raw_input().rstrip('\n').split(" "))
    graph[str(e[0])]=graph[str(e[0])].union(set([str(e[1])]))
    graph[str(e[1])]=graph[str(e[1])].union(set([str(e[0])]))
    

leaves=[]
for j in graph:
    if(len(graph[j])==1):
        leaves.append(j)


paths=[]
for i in range(len(leaves)):
    for j in range(i+1,len(leaves)):
        paths.append(list(bfs_paths(graph,leaves[i],leaves[j]))[0])
        

r=[]   
for j in paths:
    m=[]
    values = [A[int(w)-1] for w in j]
    for k in range(len(values)):
        
        if(sum(values[:k])>sum(values[k+1:])):
            a=sum(values[k:])
            m.append(a)
        else:
            a=sum(values[:k+1])
            m.append(a)
    r.append(max(m))
            
            
print(max(r))
"""graph = {'1': set(['2']),
         '2': set(['1', '3']),
         '3': set(['2'])}"""



    
