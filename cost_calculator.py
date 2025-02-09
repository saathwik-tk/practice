"""

Juspay Hiring challange:
given a weighted tree of nodes 1 to n, 1 being root children are 2i,2i+1 and so on.
all the weights are initially zero

given there are 2 types of input commands 
1 a b x ==> update the tree where all the weights of the shortest path between a and b should be increased by x
1 a b   ==> calculate the cost of traveling from a to b at this moment

INPUT:
1st line: q ==> int representing q number of queries
next q lines, represent q queries in any one of 1 a b x OR 2 a b format

OUTPUT:
the cost will be printed whenever a 2nd command is encountered.

"""

q = int(input())
commands = []
from collections import deque
 
max_element = 0
for i in range(q):
  commands.append(list(map(int,input().split(" "))))
  max_element = max(max_element, commands[i][1], commands[i][2])
  
def get_shortest_path(graph,start,end):
  parent_map = {}  # {child_val: parent_val}
  queue = deque([1])

  while queue:
      node = queue.popleft()
      if 2*node in graph:
          parent_map[2*node] = node
          queue.append(2*node)    
      if 2*node+1 in graph:
          parent_map[2*node+1] = node
          queue.append(2*node+1)

  ancestors = set()
  current_start = start
  while current_start in parent_map:
      ancestors.add(current_start)
      current_start = parent_map[current_start]
  ancestors.add(current_start)

  current_end = end
  while current_end not in ancestors:
      current_end = parent_map[current_end]

  lca = current_end

  path_start = []
  current_start = start
  while current_start != lca:
      path_start.append(current_start)
      current_start = parent_map[current_start]
  path_start.append(lca)

  path_end = []
  current_end = end 
  while current_end != lca:
      path_end.append(current_end)
      current_end = parent_map[current_end]

  return path_start + path_end[::-1]

create_graph = lambda x: {i: {2*i:0, 2*i+1:0} for i in range(1,x+1)}

def update_cost(graph, start, end, cost):
  shortest_path = get_shortest_path(graph, start, end)
  for i in range(1,len(shortest_path)):
    min_ele = min(shortest_path[i-1],shortest_path[i])
    max_ele = max(shortest_path[i-1],shortest_path[i])
    graph[min_ele][max_ele] += cost
  return graph

def get_current_cost(graph, start, end):
  current_cost=0
  shortest_path = get_shortest_path(graph, start, end)
  for i in range(1,len(shortest_path)):
    min_ele = min(shortest_path[i-1],shortest_path[i])
    max_ele = max(shortest_path[i-1],shortest_path[i])
    current_cost += graph[min_ele][max_ele]
  return current_cost

g = create_graph(max_element)
for command in commands:
  if command[0]==1:
    g = update_cost(g, command[1], command[2], command[3])
  else:
    print(get_current_cost(g, command[1], command[2]))
    
