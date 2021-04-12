# 큐 자료구조 

# 파이썬의 추상자료형 중 하나인 deque(덱)을 이용한 큐 연산
# 맨 앞고 뒤에 데이터를 삽입하고 삭제할 수 있게 해주는 자료형 (기본 큐에서 확장된 개념임)

from collections import deque

class CustomerComplaint:
    """고객 센터 문의를 나타내는 클래스"""
    def __init__(self, name, email, content):
        self.name = name
        self.email = email
        self.content = content

        
class CustomerServiceCenter:
    """고조선 호텔 서비스 센터 클래스"""
    def __init__(self):
        self.queue = deque()  # 대기 중인 문의를 저장할 큐 생성

        
    def process_complaint(self):
        """접수된 고객 센터 문의 내용 처리하는 메소드"""
        # 코드를 쓰세요
        q = self.queue
        
        if len(q) == 0:
            return print( "더 이상 대기 중인 문의가 없습니다!")
        else:
            data = q.popleft()
            return print(f'{data.name}님의 {data.content} 문의 내용 접수 되었습니다. 담당자가 배정되면 {data.email}로 연락드리겠습니다!')

        # ===== 중요 ===아래와 같이 self.queue 자체로 로직 수정 가능
        '''
        if self.queue:
            return print( "더 이상 대기 중인 문의가 없습니다!")
        else:
            data = self.queue.popleft()
            return print(f'{data.name}님의 {data.content} 문의 내용 접수 되었습니다. 담당자가 배정되면 {data.email}로 연락드리겠습니다!')
        '''

    def add_complaint(self, name, email, content):
        """새로운 문의를 큐에 추가 시켜주는 메소드"""
        new_complaint = CustomerComplaint(name, email, content)
        self.queue.append(new_complaint)

# 고객 문의 센터 인스턴스 생성
center = CustomerServiceCenter()

# 문의 접수한다
center.add_complaint("강영훈", "younghoon@codeit.com", "음식이 너무 맛이 없어요")

# 문의를 처리한다
center.process_complaint()
center.process_complaint()

# 문의 세 개를 더 접수한다
center.add_complaint("이윤수", "yoonsoo@codeit.kr", "에어컨이 안 들어와요...")
center.add_complaint("손동욱", "dongwook@codeit.us", "결제가 제대로 안 되는 거 같군요")
center.add_complaint("김현승", "hyunseung@codeit.ca", "방을 교체해주세요")

# 문의를 처리한다
center.process_complaint()
center.process_complaint()