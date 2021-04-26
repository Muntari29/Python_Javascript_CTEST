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
    
        # 경우 2 : 지우려는 노드가 하나의 자식만 있는 노드인 경경우
        # 2- 1 : 지우려는 노드가 왼쪽 자식 노드만 가지고 있는 경우
        elif node_to_delete.left_child is not None and node_to_delete.right_child is None:
            # 지우려는 노드가 왼쪽 자식만 가진 루트 노드일 경우
            if node_to_delete is self.root:
                self.root = node_to_delete.left_child
                self.root.parent = None
            # 지우려는 노드가 부모 노드에 왼쪽에 위치하는 경우
            elif node_to_delete.data < parent_node.data:
                parent_node.left_child = node_to_delete.left_child
                node_to_delete.left_child.parent = parent_node
            # 지우려는 노드가 부모 노드에 오른쪽에 위치하는 경우
            else:
                parent_node.right_child = node_to_delete.left_child
                node_to_delete.left_child.parent = parent_node


        # 2-2 : 지우려는 노드가 오른쪽 자식 노드만 가지고 있는 경우
        elif node_to_delete.left_child is None:  # 지우려는 노드가 오른쪽 자식만 있을 때:
            # 지우려는 노드가 오른쪽 자시만 가진 루트 노드일 경우
            if node_to_delete is self.root:
                self.root = node_to_delete.right_child
                self.root.parent = None
            # 지우려는 노드가 부모 노드에 왼쪽에 위치하는 경우
            elif node_to_delete.data > parent_node.data:
                parent_node.left_child = node_to_delete.right_child
                node_to_delete.right_child.parent = parent_node
            # 지우려는 노드가 부모 노드에 오른쪽에 위치하는 경우
            else:
                parent_node.right_child = node_to_delete.right_child
                node_to_delete.right_child.parent = parent_node

        # 경우 3: 지우려는 노드가 2개의 자식이 있을 때
        # 지우려는 노드의 오른쪽 자식 노드를 이용해 successor 노드를 찾는다.
        else:
            successor_node = self.find_min(node_to_delete.right_child)
            node_to_delete.data = successor_node.data
            
            """ solution_1 """
            # 3-1 : successor 노드가 삭제하려는 노드의 오른쪽 부분 트리에서  특정 부모 노드 아래 위치하는 경우
            if successor_node is successor_node.parent.left_child:
                # if else문을 사용할 필요없이 successor 노드가 오른쪽 자식 노드가 없다면 알아서 None으로 지정된다.
                # successor 노드가 오른쪽 자식 노드를 갖는경우와 갖지 않는 경우를 한 줄로 표현한 것이다.
                successor_node.parent.left_child = successor_node.right_child
            # 3-2 : successor 노드가 삭제하려는 노드의 바로 밑 오른쪽 자식인 경경우
            else:
                # 위와 마찬가지로 successor 노드가 오른쪽 자식 노드를 갖는 경우와 갖지 않는 경우를 한 줄로 표현한 것이다. 
                successor_node.parent.right_child = successor_node.right_child
            
            # 추가 조건
            # successor가 오른쪽 자식 노드를 갖는 경우 만을 따로 취급하여 부모 노드를 새롭게 지정해준다.
            if successor_node.right_child is not None:
                successor_node.right_child.parent = successor_node.parent
            
            """ solution_2 """
            # 3-1 : successor 노드가 삭제하려는 노드의 바로 밑 오른쪽 자식인 경경우
            if successor_node is node_to_delete.right_child:
                if successor_node.right_child is not None:
                    node_to_delete.right_child = successor_node.right_child
                    successor_node.right_child.parent = node_to_delete
                successor_node.parent = None
            # 3-2 : successor 노드가 삭제하려는 노드의 오른쪽 부분 트리에서  특정 부모 노드 아래 위치하는 경우
            else:
                if successor_node.right_child is not None:
                    successor_node.right_child.parent = successor_node.parent
                    successor_node.parent.left_child = successor_node.right_child
                successor_node.parent.left_child = None
                successor_node.parent = None
        
    def search(self, data):
        """이진 탐색 트리 탐색 메소드, 찾는 데이터를 갖는 노드가 없으면 None을 리턴한다"""
        temp = self.root  # 탐색용 변수, root 노드로 초기화
    
        # 원하는 데이터를 갖는 노드를 찾을 때까지 돈다
        while temp is not None:
            # 원하는 데이터를 갖는 노드를 찾으면 리턴
            if data == temp.data:
                return temp
            # 원하는 데이터가 노드의 데이터보다 크면 오른쪽 자식 노드로 간다
            if data > temp.data:
                temp = temp.right_child
            # 원하는 데이터가 노드의 데이터보다 작으면 왼쪽 자식 노드로 간다
            else:
                temp = temp.left_child
    
        return None # 원하는 데이터가 트리에 없으면 None 리턴


    @staticmethod
    def find_min(node):
        """(부분)이진 탐색 트리의 가장 작은 노드 리턴"""
        # 코드를 쓰세요
        temp = node  # 탐색용 변수, 파라미터 node로 초기화

        # temp가 node를 뿌리로 갖는 부분 트리에서 가장 작은 노드일 때까지 왼쪽 자식 노드로 간다
        while temp.left_child is not None:
            temp = temp.left_child      

        return temp  