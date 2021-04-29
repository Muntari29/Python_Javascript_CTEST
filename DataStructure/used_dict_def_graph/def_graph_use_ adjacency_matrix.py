# 인접 행렬을 이용한 그래프의 엣지 구현하기
# 편의상 노드를 이용하지 않음


# 모든 요소를 0으로 초기화시킨 크기 6 x 6 인접 행렬
adjacency_matrix = [[0 for i in range(6)] for i in range(6)]

# 코드를 쓰세요
adjacency_matrix[0][1], adjacency_matrix[1][0] = 1 , 1
adjacency_matrix[0][2], adjacency_matrix[2][0] = 1 , 1
adjacency_matrix[1][5], adjacency_matrix[5][1] = 1 , 1
adjacency_matrix[1][3], adjacency_matrix[3][1] = 1 , 1
adjacency_matrix[2][5], adjacency_matrix[5][2] = 1 , 1
adjacency_matrix[3][5], adjacency_matrix[5][3] = 1 , 1
adjacency_matrix[3][4], adjacency_matrix[4][3] = 1 , 1
adjacency_matrix[4][5], adjacency_matrix[5][4] = 1 , 1
print(adjacency_matrix)
#
[
[0, 1, 1, 0, 0, 0],
[1, 0, 0, 1, 0, 1],
[1, 0, 0, 0, 0, 1],
[0, 1, 0, 0, 1, 1],
[0, 0, 0, 1, 0, 1],
[0, 1, 1, 1, 1, 0]
]