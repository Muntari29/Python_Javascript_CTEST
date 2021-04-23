# 힙 => heapify 구현

def swap(tree, index_1, index_2):
    """완전 이진 트리의 노드 index_1과 노드 index_2의 위치를 바꿔준다"""
    temp = tree[index_1]
    tree[index_1] = tree[index_2]
    tree[index_2] = temp


def heapify(tree, index, tree_size):
    """heapify 함수"""

    # 왼쪽 자식 노드의 인덱스와 오른쪽 자식 노드의 인덱스를 계산
    left_child_index = 2 * index
    right_child_index = 2 * index + 1

    # 풀이 1
    if 0 < left_child_index < len(tree) and 0 < right_child_index < len(tree):
        max_node = max(tree[index], tree[left_child_index], tree[right_child_index])
        if max_node != tree[index]:
            if tree[left_child_index] > right_child_index:
                swap(tree, index, left_child_index)
                heapify(tree, left_child_index, len(tree))
            else:
                swap(tree, index, right_child_index)
                heapify(tree, right_child_index, len(tree))
       
    # 풀이 2
	# 이미 left, right 인덱스를 알고 있는 상황에서 max 메서드를 추가하는건 불필요한 탐색이 추가되는 샘이다.
    # max 없는 풀이
    
    # 부모 노드가 가장 크다는 가정으로 시작
    max_node_idx = index
    
    # 왼쪽 자식 검사
    if 0 < left_child_index < tree_size and tree[max_node_idx] < tree[left_child_index]:
        max_node_idx = left_child_index
        
    # 오른쪽 자식 검사
    if 0 < right_child_index < tree_size and tree[max_node_idx] < tree[right_child_index]:
        max_node_idx = right_child_index
        
    # 부모 노드가 가장 큰줄 알았는데, 부모노드가 가장 크지 않았다!!
    if max_node_idx != index:
        swap(tree, index, max_node_idx)
        heapify(tree, max_node_idx, tree_size)



# 실행 코드
tree = [None, 15, 5, 12, 14, 9, 10, 6, 2, 11, 1]  # heapify하려고 하는 완전 이진 트리
heapify(tree, 2, len(tree))  # 노드 2에 heapify 호출
print(tree) 