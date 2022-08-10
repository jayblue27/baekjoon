class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        '''
        노드 개수와 무방향 그래프를 입력받아 트리가 최소 높이가 되는 루트의 목록을 리턴하라.
        
        무방향 그래프 - root는 둘다 가능하다
        
        # 풀이법 - 단계별 리프노드 제거
        모든 리프들을 제거 해주면서 root를 거꾸로 찾아간다. 
        '''
        
        if n <= 1:
            return [0]
        
        # 양방향 그래프 구성 (무방향 그래프이기 때문에)
        graph = collections.defaultdict(list)
        for i,j in edges:
            graph[i].append(j)
            graph[j].append(i)
        
        # 첫 번째 리프 노드 추가
        leaves = []
        for i in range(n+1):
            if len(graph[i]) == 1: 
                leaves.append(i)
        
        # 루트 노트만 남을 때까지 반복 제거
        while n > 2:
            n -= len(leaves) 
            new_leaves = []
            for leaf in leaves:
                neighbor = graph[leaf].pop()
                graph[neighbor].remove(leaf)
                
                # 그 다음 leaf node 추가
                if len(graph[neighbor]) == 1:
                    new_leaves.append(neighbor)
            leaves = new_leaves
            
        return leaves
            
        
        