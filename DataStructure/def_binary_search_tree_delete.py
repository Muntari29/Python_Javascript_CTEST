# 이진 탐색 트리 삭제 구현

class BinarySearchTree:
    """이진 탐색 트리 클래스"""
    def __init__(self):
        self.root = None


    def delete(self, data):
        """이진 탐색 트리 삭제 메소드"""
        node_to_delete = self.search(data)  # 삭제할 노드를 가지고 온다
        parent_node = node_to_delete.parent  # 삭제할 노드의 부모 노드

        # 지우려는 노드가 리프 노드인 경우
        if node_to_delete.left_child is None and node_to_delete.right_child is None:
            # 지우려는 노드가 리프노드이면서 동시에 부모 노드 일 경우
            if node_to_delete is self.root:
                self.root = None
            # 지우려는 노드가 부모 노드의 왼쪽 자식 노드인 경우
            if parent_node.left_child == node_to_delete:
                parent_node.left_child = None
            # 지우려는 노드가 부모 노드의 오른쪽 자식 노드인 경우    
            else:
                parent_node.right_child = None
        

    @staticmethod
    def find_min(node):
        """(부분)이진 탐색 트리의 가장 작은 노드 리턴"""
        # 코드를 쓰세요
        temp = node  # 탐색용 변수, 파라미터 node로 초기화

        # temp가 node를 뿌리로 갖는 부분 트리에서 가장 작은 노드일 때까지 왼쪽 자식 노드로 간다
        while temp.left_child is not None:
            temp = temp.left_child      

        return temp  