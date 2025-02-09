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
for i in range(q):
  commands.append(list(map(int,input().split(" "))))
  
def shortest_path(graph):
  path_arr=[]
  return path_arr

def create_graph():
  g={}
  return g

def update_cost(graph, start, end, cost):
  return

def get_current_cost(graph, start, end):
  current_cost=0
  return current_cost

g=create_graph()
for command in commands:
  if command[0]==1:
    update_cost(g, command[1], command[2], command[3])
  else:
    print(get_current_cost(g, command[1], command[2]))
    
