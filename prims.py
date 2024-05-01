# Prims Algorithm

V = 5

G = [
    [0, 4, 5, 8, 3],
    [4, 0, 0, 2, 0],
    [5, 0, 0, 0, 4],
    [8, 2, 0, 0, 1],
    [3, 0, 4, 1, 0]
]

selected_node = [0, 0, 0, 0, 0]

no_edge = 0

total_weight = 0

selected_node[0] =True

print("Prims Algorithm :- ")
print("Edge  Weight\n")

while ( no_edge < V - 1):
    
    minimum = float('inf')
    x = 0
    y = 0
    for i in range(V):
        if selected_node[i]:
            for j in range(V):
                if (not selected_node[j] and G[i][j]):
                    minimum > G[i][j]
                    minimum = G[i][j]
                    x = i
                    y = j
                    
    print(str(x) + " - "+ str(y) + " :- "+ str(G[x][y]))
    selected_node[y] =True
    no_edge += 1 
    total_weight += G[x][y]
    
print("\nTotal Weight Of MST :- " ,total_weight)
