from collections import deque
from subway_graph import create_station_graph

def bfs(graph, start_node):
    """시작 노드에서 bfs를 실행하는 함수"""
    # 이 함수의 결과로 주어진 노드(탐색기준)과 인접해있는 노드들은 방문표시가 True로 변경되며
    # True로 변경됨은 주어진 노드와 연결(경로)되어있는다는 의미이다.
    queue = deque()  # 빈 큐 생성

    # 탐색을 한번만하지 않기에, 일단 모든 노드를 방문하지 않은 노드로 표시
    for station_node in graph.values():
        station_node.visited = False
    
    # 시작점 노드를 방문 표시 해줌
    start_node.visited = True
     # 큐에 시작점 노드를 넣은 후 반복문 시작
    queue.append(start_node)
    
    # 큐에 노드가 없을때까지 반복
    while queue:
        # 큐의 맨앞 데이터 추출
        queue_frist_node = queue.popleft()

        # 맨앞 추출한 데이터(여기선 노드) 를 이용해 
        # 추출한 노드의 인접해있는 노드들을 돌면서 방문 여부를 변경함
        # 만약 방문하지 않은(false)일 경우 큐에 넣고 큐에 노드가 없을때까지 반반복
        for adjacent_node in queue_frist_node.adjacent_stations:
            if not adjacent_node.visited:
                adjacent_node.visited = True
                queue.append(adjacent_node)


stations = create_station_graph("./new_stations.txt")  # stations.txt 파일로 그래프를 만든다

# stations 딕셔너리의 키 = 강남과 일치하는 value, 즉 station_node를 저장
gangnam_station = stations["강남"]

# 강남역과 경로를 통해 연결된 모든 노드를 탐색
bfs(stations, gangnam_station)

# 강남역과 서울 지하철 역들이 연결됐는지 확인
print(stations["강동구청"].visited)
print(stations["평촌"].visited)
print(stations["송도"].visited)
print(stations["개화산"].visited)

# 강남역과 대전 지하철 역들이 연결됐는지 확인
print(stations["반석"].visited)
print(stations["지족"].visited)
print(stations["노은"].visited)
print(stations["(대전)신흥"].visited)