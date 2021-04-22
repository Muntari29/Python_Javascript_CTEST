# 힙 더맵게

# 부모 노드와 자식 노드 위치 변경
def swap(tree, idx_1, idx_2):
        temp = tree[idx_1]
        tree[idx_1] = tree[idx_2]
        tree[idx_2] = temp

def heapify(tree, idx, tree_size):
        
        left_node_idx = idx * 2
        right_node_idx = idx * 2 + 1
        
        # 부모노드의 인덱스가 가장 큰 값이라 가정함
        max_node_idx = idx
        
        # 여기서 부등호를 변경할 경우 내림차순 오름차순 선택이 가능하다.
        if 0 < left_node_idx < tree_size and tree[idx] > tree[left_node_idx]:
            max_node_idx = left_node_idx
        
        if 0 < right_node_idx < tree_size and tree[idx] > tree[right_node_idx]:
            max_node_idx = right_node_idx

        # 부모가 가장 큰 값이 아닌 경우
        if max_node_idx != idx:
            swap(tree, idx, max_node_idx)
            heapify(tree, max_node_idx, tree_size)

# 힙 정렬
def heap_sort(tree):
    tree_size = len(tree)
    for idx in range(tree_size, 0, -1):
        heapify(tree, idx, tree_size)

    for idx in range(tree_size-1, 0, -1):
        swap(tree, 1, idx)
        heapify(tree, 1, idx)
    

def solution(scoville, K):
    answer = 0
    count = 1
    tree = [None] + scoville
    '''heapify 반복으로 힙 트리 만들어주기'''
    for i in range(len(tree), 0, -1):
        heapify(tree, i, len(tree))
    print(tree)
    heap_sort(tree)
    print(tree)

    while True:
        print(tree)
        number_1 = tree.pop()
        number_2 = tree.pop()
        scoville_number = number_1 + (number_2 * 2)
        tree.append(scoville_number)
        answer += 1
        
        if scoville_number >= 7:
            tree.append(scoville_number)
            answer += 1
            break
        tree.append(scoville_number)   

    return print(answer)