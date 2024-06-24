# Problem: From adjacency matrix to adjacency lists - https://basecamp.eolymp.com/en/problems/3981

num_vertices = int(input().strip())

adj_matrix = []
for _ in range(num_vertices):
    adj_matrix.append(list(map(int, input().strip().split())))

for i in range(num_vertices):
    adj_list = []
    for j in range(num_vertices):
        if adj_matrix[i][j] == 1:
            adj_list.append(j + 1)
    print(len(adj_list), *adj_list)
