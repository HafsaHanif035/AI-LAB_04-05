
#LAB 04
#Activity 01
class Node:
    def __init__(self, state, parent, actions, totalCost):
        self.state = state
        self.parent = parent
        self.actions = actions
        self.totalCost = totalCost
        


def actionSequence(graph, initialState, goalState):
    sol = [goalState]
    currentParent = graph[goalState].parent
    while currentParent!=None:
        sol.append(currentParent)
        currentParent=graph[currentParent].parent
    sol.reverse()
    return sol

def DFS():
    initialState = 'D'
    goalState = 'C'
    
    graph = {'A' : Node('A', None, ['B', 'C', 'E'], None),
         'B' : Node('B', None, ['A', 'D', 'E'], None),
         'C' : Node('C', None, ['A', 'F', 'G'], None),
         'D' : Node('D', None, ['B', 'E'], None),
         'E' : Node('E', None, ['A', 'B', 'D'], None),
         'F' : Node('F', None, ['C'], None),
         'G' : Node('G', None, ['C'], None)
        }
    frontier = [initialState]
    explored = []
    
    while len(frontier)!=0:
        currentNode = frontier.pop(len(frontier)-1)
        print(currentNode)
        explored.append(currentNode)
        currentChildren = 0
        for child in graph[currentNode].actions:
            if child not in frontier and child not in explored:
                graph[child].parent = currentNode
                if graph[child].state==goalState:
                    print(explored)
                    return actionSequence(graph, initialState, goalState)
                currentChildren = currentChildren+1
                frontier.append(child)
        if currentChildren==0:
            del explored[len(explored)-1]
            
sol=DFS()
print(sol)

 
# Lab Task 1
class Node :

    def __init__(self,state,parent,actions,totalCost):
        self.state=state
        self.parent=parent
        self.actions=actions
        self.totalCost=totalCost
def DFS():
    initial= input("Enter initial Node: ")
    goal = input("Enter destination Node: ")
    
    graph={
        'Oradea' : Node('Oradea',None,['Zerind','Sibiu'],[71,151] ),
        'Zerind' : Node('Zerind',None,['Arad', 'Oradea'],[75,71 ]),
        'Arad' : Node('Arad',None,['Zerind','Timisoara','Sibiu'],[75,118,140] ),
        'Sibiu' : Node('Sibiu',None,['Fagaras','Rimnicu Vilcea','Oradea','Arad'],[99,80,151,140] ),
        'Fagaras' : Node('Fagaras',None,['Sibiu','Bucharest'],[99,211] ),
        'Bucharest' : Node('Bucharest',None,['Fagaras','Pitesti','Urziceni','Giurgiu'],[211,101,85,90] ),
        'Pitesti' : Node('Pitesti',None,['Rimnicu Vilcea','Bucharest','Craiova'],[97,101,138] ),
        'Urziceni' : Node('Urziceni',None,['Bucharest','Hirsova','Vaslui'],[85,98,142] ),
        'Hirsova' : Node('Hirsova',None,['Urziceni','Eforie'],[98,86] ),
        'Timisoara':Node('Timisoara',None,['Lugoj','Arad'],[111,118]),
        'Lugoj':Node('Lugoj',None,['Mehadia','Timisoara'],[70,111]),
        'Mehadia':Node('Mehadia',None,['Drobeta','Lugoj'],[75,70]),
        'Rimnicu Vilcea':Node('Rimnicu Vilcea',None,['Sibiu','Pitesti'],[70,111]),
        'Drobeta' : Node('Drobeta',None,['Craiova','Mehadia'],[120,75] ),
        'Craiova' : Node('Craiova',None,['Pitesti','Rimnicu Vilcea'],[138,146] ),
        'Eforie' : Node('Eforie',None,['Hirsova'],[86] ),
        'Vaslui' : Node('Vaslui',None,['Urziceni','Iasi'],[142,92] ),
        'Iasi' : Node('Iasi',None,['Vaslui','Neamt'],[92,87] ),
        'Giurgiu' : Node('Giurgiu',None,[],[]),
        'Neamt' : Node('Neamt',None,[],[] ),
        }
    front=[initial]
    explore=[]
    while(len(front)!=0):
         cNode=front.pop(len(front)-1)
         print (cNode)
         explore.append(cNode)
         cChild=0
         
         for i in graph[cNode].actions :
            if i not in front and i not in explore : 
                if graph[i].state==goal:
                    return actionSequence(graph,initial,goal)
                cChild=cChild+1
                front.append(i)
         if cChild==0:
            del explore[len(explore)-1]
def actionSequence(graph,initial,goal):
    sol=[goal]
    cp=graph[goal].parent
    while cp!=None:
        sol.append(cp)
        cp=graph[cp].parent
    sol.reverse()
    return sol

sol=DFS()
print(sol)
          

class Trie:
    def __init__(self):
        self.character = {}
        self.isLeaf = False  
 
 
# Iterative function to insert a string into a Trie
def insert(root, s):
    # starting from the root node
    curr = root
 
    for ch in s:
        curr = curr.character.setdefault(ch, Trie())
 
    curr.isLeaf = True
 
 
# (top, right, bottom, left, and four diagonal moves)
row = [-1, -1, -1, 0, 1, 0, 1, 1]
col = [-1, 1, 0, -1, -1, 1, 0, 1]
 
def isSafe(x, y, processed, board, ch):
    return (0 <= x < len(processed)) and (0 <= y < len(processed[0])) and \
           not processed[x][y] and (board[x][y] == ch)
 

def searchBoggle(root, board, i, j, processed, path, result):
    if root.isLeaf:
        result.add(path)
 
    processed[i][j] = True
 
    for key, value in root.character.items():
 
        for k in range(len(row)):
 
            if isSafe(i + row[k], j + col[k], processed, board, key):
                searchBoggle(value, board, i + row[k], j + col[k],
                             processed, path + key, result)
 
    processed[i][j] = False
 
 
def searchInBoggle(board, words):
    
    result = set()
     # base case
    if not board or not len(board):
        return
 
    
    root = Trie()
    for word in words:
        insert(root, word)
 
    # performing `M × N` board
    (M, N) = (len(board), len(board[0]))
 
    processed = [[False for x in range(N)] for y in range(M)]
 
    # consider each of the character in the matrix
    for i in range(M):
        for j in range(N):
            ch = board[i][j]  
 
            if ch in root.character:
                searchBoggle(root.character[ch], board, i, j, processed, ch, result)
 
    return result

board = [
    ['M', 'S', 'E', 'F'],
    ['R', 'A', 'T', 'D'],
    ['L', 'O', 'N', 'E'],
    ['K', 'A', 'F', 'B']
  ]

words = ['START', 'NOTE', 'SAND', 'STONED']
searchInBoggle(board, words)

validWords = searchInBoggle(board, words)
print(validWords)


#LAB 04
# Lab Task 1
graph = {
        'arad':['sibiu', 'zerind', 'timisoara'],
        'sibiu':['oradea', 'fagaras', 'rimnicu'],
        'zerind':['arad', 'oradea'],
        'timisoara':['arad', 'lugoj'],
        'oradea':['zerind', 'sibiu'],
        'fagaras':['sibiu', 'bucharest'],
        'lugoj':['timisoara', 'mehadia'],
        'mehadia':['lugoj', 'drobeta'],
        'drobeta':['mehadia', 'craiova'],
        'craiova':['drobeta', 'riminica','pitesti'],
        'riminica':['sibui', 'pitesti','craiova'],
        'pitesti':['riminica', 'craiova','bucharest'],
        'bucharest':['fagaras', 'pitesti','urziceni'],
        'urziceni':['bucharest', 'hirsova','vaslui'],
        'hirsova':['urziceni', 'eforie'],
        'vaslui':['isai', 'urzicini'],
        'eforie':['hirsova'],
        'isai':['neamt', 'vaslui'],
        'giurgui':['bucharest'],
        'neamt':['isai']
        }
def DFS(parent,destination,graph,depth):
    print("The path for this is:: ",parent) # Travesing of tree
    if parent==destination: # Checking whether it is reaching in 1st itteration to goal
        return True
    if depth<=0: # The limit setted was reached to its limit
        return False
    for childs in graph[parent]: # Traversing through childs of parents
        if DFS(childs,destination,graph,depth-1):
            return True
    return False
            # we will call the dfs function for th same functionallity
        # but the parent will be replaced by child node as we are exploring it and depth will become -1 
        # because we are traversing in depth.
def IterativeDeep(parent,destination,graph,depth): # For IDS we will create this
    for i in range(depth): # Travese depending on number of depths
        if DFS(parent,destination,graph,i): # i will traverse from i to maxdepth i.e.0,1.2.3...n
            return True
    return False
if not IterativeDeep('arad','bucharest',graph,4):
    print("No path found!! ")
else:
    print("We found a Path!! ")
   
row = [-1, -1, -1, 0, 1, 0, 1, 1]
col = [-1, 1, 0, -1, -1, 1, 0, 1]
 
 
# Function to check if it is safe to go to cell (x, y) from the current cell.
# The function returns false if (x, y) is not valid matrix coordinates
# or cell (x, y) is already processed.
def isSafe(x, y, processed):
    return (0 <= x < len(processed)) and (0 <= y < len(processed[0]))\
        and not processed[x][y]
 
 
# A recursive function to generate all possible words in a boggle
def searchBoggle(board, words, result, processed, i, j, path=''):
    # mark the current node as processed
    processed[i][j] = True
 
    # update the path with the current character and insert it into the set
    path += board[i][j]
 
    # check whether the path is present in the input set
    if path in words:
        result.add(path)
 
    # check for all eight possible movements from the current cell
    for k in range(len(row)):
        # skip if a cell is invalid, or it is already processed
        if isSafe(i + row[k], j + col[k], processed):
            searchBoggle(board, words, result, processed, i + row[k], j + col[k], path)
 
    # backtrack: mark the current node as unprocessed
    processed[i][j] = False
 
 
def searchInBoggle(board, words):
 
    # construct a set to store valid words constructed from the boggle
    result = set()
 
    # base case
    if not board or not len(board):
        return
 
    # `M × N` board
    (M, N) = (len(board), len(board[0]))
 
    # construct a boolean matrix to store whether a cell is processed or not
    processed = [[False for x in range(N)] for y in range(M)]
 
    # generate all possible words in a boggle
    for i in range(M):
        for j in range(N):
            # consider each character as a starting point and run DFS
            searchBoggle(board, words, result, processed, i, j)
 
    return result
 
 
if __name__ == '__main__':
 
    board = [
        ['M', 'S', 'E'],
        ['R', 'A', 'T'],
        ['L', 'O', 'N']
    ]
 
    words = ['START', 'NOTE', 'SAND', 'STONE']
 
    validWords = searchInBoggle(board, words)
    print("The Valid Words Are:: ")
    print(validWords)
