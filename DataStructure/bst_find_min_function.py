# 이진 탐색 트리에서의 find_min 정적메서드 함수 구현

class Node:
    """이진 탐색 트리 노드 클래스"""
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.right_child = None
        self.left_child = None

class BinarySearchTree:
    """이진 탐색 트리 클래스"""
    def __init__(self):
        self.root = None


    # 정적메서드로 구현
    # 인스턴스 내용과 상관없이 결과를 도출할때 사용 블로그 포스팅 참고
    @staticmethod
    def find_min(node):
        """(부분)이진 탐색 트리의 가장 작은 노드 리턴"""
        compare_node = node
        
        # solution_1
        while compare_node is not None:
            if compare_node.left_child is None:
                return compare_node
            compare_node = compare_node.left_child
        
        return None
        
        # solution_2
        while compare_node.left_child is not None:
            compare_node = compare_node.left_child
        
        return compare_node
