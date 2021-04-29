# 딕셔너리를 활용하여 그래프 구현하기

class StationNode:
    """간단한 지하철 역 노드 클래스"""
    def __init__(self, station_name):
        self.station_name = station_name

def create_station_nodes(input_file):
    """input_file에서 데이터를 읽어 와서 지하철 그래프 노드들을 리턴하는 함수"""
    stations = {}  # 지하철 역 노드들을 담을 딕셔너리

    # 파라미터로 받은 input_file(문자열타입) 해당 이름을 갖는파일을 연다
    with open(input_file) as stations_raw_file:
        for line in stations_raw_file:  # 파일을 한 줄씩 받아온다
            # 앞 뒤 공백 삭제후, -를 기준으로 나눈 리스트로 만듬.
            subway_line = line.strip().split("-")
            
            # subway_line 배열을 반복
            # 요소별로 양옆의 여백(띄어쓰기)를 다시 한번 제거
            for name in subway_line:
                station_name = name.strip()
                stations[station_name] = StationNode(station_name)

    return stations


stations = create_station_nodes("/Users/munseunghui/playground/codingtest/Python_Javascript_CTEST/DataStructure/used_dict_def_graph/test_stations.txt")  # stations.txt 파일로 그래프 노드들을 만든다

# stations에 저장한 역들 이름 출력 (채점을 위해 역 이름 순서대로 출력)
for station in sorted(stations.keys()):
    print(stations[station].station_name)