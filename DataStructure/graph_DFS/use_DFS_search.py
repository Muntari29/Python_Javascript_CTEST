# 예시를 위해 visited = 0으로  0, 1 , 2의 값을 가질 수 있는 인스턴스로 사용하였다.
# 오로지 예시로 인한 수정 사항으로 BFS에서와 마찬가지로 T/F로 충분히 나타 낼 수 있다.
# DFS 탐색 알고리즘 구현

from collections import deque
from subway_graph import *

def dfs(graph, start_node):
    """dfs 함수"""
    stack = deque()  # 빈 스택 생성

    # 모든 노드를 처음 보는 노드로 초기화
    for station_node in graph.values():
        station_node.visited = 0

    # 문제 예시의 편의를 위한것으로 BFS와 마찬가지로 True/False로도 나타낼 수 있다.
    # BFS와 DFS의 가장 큰 차이는 큐/스택 추상 자료형을 이용해 구현한다는 것이다.
    
    # 옅은 회색 표시 후, 스택에 넣어준다.
    start_node.visited = 1
    stack.append(start_node)
    
    # 스택이 빌때까지 반복
    while stack:
        # 스택의 맨 뒤 데이터 삭제(추출)
        stack_last_node = stack.pop()
        # 노드를 추출해오며 해당 노드에 방문 표시를 해준다.
        stack_last_node.visited = 2
        
        # 추출한 노드의 인접 리스트를 돌며
        # 방문하지 않은 노드(0) 일 경우 옅은 회색 표시와 함께 스택에 넣어준다.
        for neighbor_node in stack_last_node.adjacent_stations:
            if neighbor_node.visited == 0:
                neighbor_node.visited = 1
                stack.append(neighbor_node)

stations = create_station_graph("./new_stations.txt")  # stations.txt 파일로 그래프를 만든다

gangnam_station = stations["강남"]

# 강남역과 경로를 통해 연결된 모든 노드를 탐색
dfs(stations, gangnam_station)

# 강남역과 서울 지하철 역들 연결됐는지 확인
print(stations["강동구청"].visited)
print(stations["평촌"].visited)
print(stations["송도"].visited)
print(stations["개화산"].visited)

# 강남역과 대전 지하철 역들 연결됐는지 확인
print(stations["반석"].visited)
print(stations["지족"].visited)
print(stations["노은"].visited)
print(stations["(대전)신흥"].visited)