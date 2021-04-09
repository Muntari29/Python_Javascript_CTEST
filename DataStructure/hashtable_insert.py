# 해시테이블 체이닝을 사용하기 위한 링크드리스트 임포트
from hash1 import LinkedList

# case1 
class HashTable:
    """해시 테이블 클래스"""
    
    def __init__(self, capacity):
        self._capacity = capacity  # 파이썬 리스트 수용 크기 저장
        self._table = [LinkedList() for _ in range(self._capacity)]  # 파이썬 리스트 인덱스에 반 링크드 리스트 저장

    def _hash_function(self, key):
        """
        주어진 key에 나누기 방법을 사용해서 해시된 값을 리턴하는 메소드
        주의: key는 파이썬 불변 타입이여야 한다.
        """
        return hash(key) % self._capacity


    def look_up_value(self, key):
        """
        주어진 key에 해당하는 데이터를 리턴하는 메소드
        """
        """
        크게 단계를 나눈다면
        키값으로 해시테이블의 인덱스를 찾는다
        인덱스를 통해 해당 인덱스에 위치한 링크드 리스트를 가져온다
        링크드 구성시 사용하였던 메서드를 활용하여 해당 링크드 리스트에서 주어진 키 값을가지고 있는 노드를 가가져온다
        만약 노드가 없다면 해당 링크드 리스트 안에 키값에 해당하는 노드가 없다는 뜻
        노드가 있다면 해당 노드의 값을 찾으면 된다
        """
        # 코드를 쓰세요
        index = self._hash_function(key)
        # 인덱스를 통해 해당 인덱스에 위치한 링크드 리스틑를 가져옴
        table_linked_list = self._table[index]
        # 링크드 리스트를 통해 해당 Key 값을 가지고 있는 노드가 있는지 확인함
        data = table_linked_list.find_node_with_key(key)
        
        if data is None:
           return None
        # 해당 노드의 값을 출력
        return table_linked_list.find_node_with_key(key).value
        
    def insert(self, key, value):
        """
        새로운 key - value 쌍을 삽입시켜주는 메소드
        이미 해당 key에 저장된 데이터가 있으면 해당 key에 해당하는 데이터를 바꿔준다
        """
        """
        위 내용에서 더 나아가서
        키값과 일치하는 노드가 있다면 해당 노드의 값을 입력한 값으로 변경해주면 된다.
        키값과 일치하는 노드가 없다면! appned 메소드를 이용해 링크드 리스트의 맨뒤에 추가해준다!
        """
        index = self._hash_function(key)
        
        table_linked_list = self._table[index]
        
        data = table_linked_list.find_node_with_key(key)
        if data is None:
            table_linked_list.append(key, value)
        else:
            data.value = value

    def __str__(self):
        """해시 테이블 문자열 메소드"""
        res_str = ""

        for linked_list in self._table:
            res_str += str(linked_list)

        return res_str[:-1]

    
 
test_scores = HashTable(50)  # 시험 점수를 담을 해시 테이블 인스턴스 생성

# 여러 학생들 이름과 시험 점수 삽입
test_scores.insert("현승", 85)
test_scores.insert("영훈", 90)
test_scores.insert("동욱", 87)
test_scores.insert("지웅", 99)
test_scores.insert("신의", 88)
test_scores.insert("규식", 97)
test_scores.insert("태호", 90)

print(test_scores)

# key인 이름으로 특정 학생 시험 점수 검색
print(test_scores.look_up_value("현승"))
print(test_scores.look_up_value("태호"))
print(test_scores.look_up_value("영훈"))

# 학생들 시험 점수 수정
test_scores.insert("현승", 10)
test_scores.insert("태호", 20)
test_scores.insert("영훈", 30)

print(test_scores)

# Case 2  => 메서드 추가

class HashTable2:
    """해시 테이블 클래스"""
    
    def __init__(self, capacity):
        self._capacity = capacity  # 파이썬 리스트 수용 크기 저장
        self._table = [LinkedList() for _ in range(self._capacity)]  # 파이썬 리스트 인덱스에 반 링크드 리스트 저장

    def _hash_function(self, key):
        """
        주어진 key에 나누기 방법을 사용해서 해시된 값을 리턴하는 메소드
        주의: key는 파이썬 불변 타입이여야 한다.
        """
        return hash(key) % self._capacity


    def _get_linked_list(self, key):
        """
        주어진 key에 해당하는 링크드 리스트를 리턴하는 메서드
        """
        index = self._hash_function(key)
        table_linked_list = self._table[index]
        if table_linked_list is None:
            return None
        return table_linked_list
        
    def _get_table_linked_list_node(self, key):
        """
        주어진 key에 해당하는 링크드 리스트 안, 노드를 리턴하는 메서드
        편의상 None 일경우는 제외함
        """
        table_linked_list = self._get_linked_list(key)
        return table_linked_list.find_node_with_key(key)
        
    def look_up_value(self, key):
        """
        주어진 key에 해당하는 데이터를 리턴하는 메소드
        """
        result = self._get_table_linked_list_node(key)
        
        return result.value
        
    def insert(self, key, value):
        """
        새로운 key - value 쌍을 삽입시켜주는 메소드
        이미 해당 key에 저장된 데이터가 있으면 해당 key에 해당하는 데이터를 바꿔준다
        """
        table_linked_list = self._get_linked_list(key)
        node = self._get_table_linked_list_node(key)
        if node is None:
            table_linked_list.append(key, value)
        else:
            node.value = value


    def __str__(self):
        """해시 테이블 문자열 메소드"""
        res_str = ""

        for linked_list in self._table:
            res_str += str(linked_list)

        return res_str[:-1]

# Case 3 => 코드잇 답안

class HashTable3:
    def __init__(self, capacity):
        self._capacity = capacity  # 파이썬 리스트 수용 크기 저장
        self._table = [LinkedList() for _ in range(self._capacity)]  # 파이썬 리스트 인덱스에 반 링크드 리스트 저장

    def _hash_function(self, key):
        """
        주어진 key에 나누기 방법을 사용해서 해시된 값을 리턴하는 메소드
        주의: key는 파이썬 불변 타입이여야 한다.
        """
        return hash(key) % self._capacity


    def _get_linked_list_for_key(self, key):
        """주어진 key에 대응하는 인덱스에 저장된 링크드 리스트를 리턴하는 메소드"""
        hashed_index = self._hash_function(key)

        return self._table[hashed_index]


    def _look_up_node(self, key):
        """파라미터로 받은 key를 갖고 있는 노드를 리턴하는 메소드"""
        linked_list = self._get_linked_list_for_key(key)
        return linked_list.find_node_with_key(key)


    def look_up_value(self, key):
        """
        주어진 key에 해당하는 데이터를 리턴하는 메소드
        """
        return self._look_up_node(key).value


    def insert(self, key, value):
        """
        새로운 key - value 쌍을 삽입시켜주는 메소드
        이미 해당 key에 저장된 데이터가 있으면 해당 key에 해당하는 데이터를 바꿔준다
        """
        existing_node = self._look_up_node(key)  # 이미 저장된 key인지 확인한다

        if existing_node is not None:
            existing_node.value = value  # 이미 저장된 key면 데이터만 바꿔주고
        else:
            # 없는 key면 링크드 리스트에 새롭게 삽입시켜준다
            linked_list = self._get_linked_list_for_key(key)
            linked_list.append(key, value)

    def delete_by_key(self, key):
        """주어진 key에 해당하는 key - value 쌍을 삭제하는 메소드"""
        # 코드를 쓰세요

    def __str__(self):
        """해시 테이블 문자열 메소드"""
        res_str = ""

        for linked_list in self._table:
            res_str += str(linked_list)

        return res_str[:-1]

