#Code not working
# BFS with queue
def bfs(src):
    queue = []
    front = 0
    rear = -1
    visited = []
    
    for j in range(3) :
        visited[j] = 0
    visited[src] = 1
    rear = rear + 1
    queue[rear] = src

    
    while front <= rear:
        i = queue[front]
        front = front + 1
        
        for j in range(3):
            if adj_matrix[i][j] == 1 and visited[j] != 1:
                visited[j] = 1
                rear = rear + 1
                queue[rear] = j

    for i in range(3): 
        if visited[j] != 1:
            print("node " + j + " is not reachable")
        else:
            print("node " + j + " is reachable")


#main function
n = 3
adj_matrix = [[0, 1, 1], [1, 0, 0], [1, 0, 0]]

#int(input("Enter the number of nodes: "))

#for i in range(1, 4):
    #print("h")
    #for j in range(1, 4):
        
        #print("Enter the adjacency matrix: ")
        #a.append(int(input()))
        #adj_matrix.append(int(input()))
        
        #adj_matrix = [[int(input()) for i in range (1, n)] for j in range(1, n)]
#for i in range(1, n+1):
    #for j in range(1, n+1):   
        #print(adj_matrix[i][j], end = " ")
        #print()

src = int(input("Enter the source node: "))

#invoking the function
bfs(src)


