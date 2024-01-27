'''
1. 문제이해 
- 그래프의 간선정보가 주어짐 
- [정점의 번호, 도넛 모양 그래프의 수, 막대 모양 그래프의 수, 8자 모양 그래프의 수] 형태의 list를 return 

2. 접근방법
- 정점의 번호 및 각 모형의 그래프 수를 어떻게 카운팅 하나?

- 그래프를 특정할 수 있는 노드를 찾는다

- 점점의 번호 
    - output edge가 n개(2개 이상) input edge가 0개 인 경우
- 막대 모양 그래프
    - 가장 마지막 노드는 input edge가 1개 output edge가 0개
- 8자 모양 그래프
    - 중간에 있는 노드는 input edge가 2개 output edge가 2개
- 도넛 모양 그래프 
    - 생성된 노드의 output edge 수에서 막대모양 그래프와 8자모양 그래프의 개수를 빼서 구한다


'''

def solution(edges):
    input_count = [0 for _ in range(1000001)]
    output_count = [0 for _ in range(1000001)]
    
    created_node = -1    
    doughnut_count = 0
    stick_count = 0
    eight_count = 0
    biggest_node_num = -1
    
    # 그래프 순회하며 마지막 node 번호 획득
    # node 마다, 나가는 간선의 수, 들어오는 간선의 수 count
    for a, b in edges:
        biggest_node_num = max(biggest_node_num, a, b)
        output_count[a] += 1
        input_count[b] += 1
    
    # 1번 노드부터 마지막 노드까지 순회
    for i in range(1, biggest_node_num + 1):
        # 정점노드 판별 (나가는 간선이 2개이상, 들어오는 간선이 없다.)
        if input_count[i] == 0 and output_count[i] >= 2:
            created_node = i
        # 막대형 그래프 (나가는 간선이 없다.)
        elif input_count[i] >= 1 and output_count[i] == 0:
            stick_count += 1
        # 8자형 그래프 (나가는 간선 2개이상, 들어오는 간선 2개이상)
        elif input_count[i] >= 2 and output_count[i] == 2:
            eight_count += 1

    doughnut_count = output_count[created_node] - stick_count - eight_count
    return [created_node, doughnut_count, stick_count, eight_count]