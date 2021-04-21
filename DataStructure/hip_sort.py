# 힙 정렬 구현
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

    largest = index  # 일단 부모 노드의 값이 가장 크다고 설정

    # 왼쪽 자식 노드의 값과 비교
    if 0 < left_child_index < tree_size and tree[largest] < tree[left_child_index]:
        largest = left_child_index

    # 오른쪽 자식 노드의 값과 비교
    if 0 < right_child_index < tree_size and tree[largest] < tree[right_child_index]:
        largest = right_child_index
    
    if largest != index: # 부모 노드의 값이 자식 노드의 값보다 작으면
        swap(tree, index, largest)  # 부모 노드와 최댓값을 가진 자식 노드의 위치를 바꿔준다
        heapify(tree, largest, tree_size)  # 자리가 바뀌어 자식 노드가 된 기존의 부모 노드를대상으로 또 heapify 함수를 호출한다

def heapsort(tree):
    """힙 정렬 함수"""
    tree_size = len(tree)
    result = []
    # 힙은 위로 올라갈수록 커야하며, 부모부터 heapify를 할경우 중간에 바뀌었을때 위쪽을 다시 확인할 수없다.
    # 따라서 가장 맨 아래의 자식 노드부터 heapify를 해준다.
    # 리스트를 힙 조건에 맞게 heapify완료
    for idx in range(tree_size, 0, -1):
        heapify(tree, idx, tree_size)
    
    # 루트노드와 마지막 노드의 위치를 변경해주고 힙에서 변경된 마지막 위치의 노드를 없어졌다고  가정한다.
    # heapify의 tree_size 파라미터가 계속해서 1씩 줄어드는 파라미터로 받기 때문에 맨 마지막 인덱스는 고려하지 게되고
    # 맨 마지막 인덱스는 heapify 영역에서 벗어나 삭제된 것 처럼 간주된다!!
    for idx in range(tree_size-1, 0, -1):
        swap(tree, 1, idx)
        heapify(tree, 1, idx)


# 실행 코드
data_to_sort = [None, 6, 1, 4, 7, 10, 3, 8, 5, 1, 5, 7, 4, 2, 1]
heapsort(data_to_sort)
print(data_to_sort)