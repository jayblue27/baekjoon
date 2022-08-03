class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        '''
        prerequisites[i] =  [a, b]   -> a를 듣기 위해서는 반드시 b를 들어야 한다. 
        모든 코스를 
        '''
        # 위상정렬 - 189ms
        graph = collections.defaultdict(list) # 그래프 초기화
        indegree = [0] * numCourses # 진입차수 초기화 
        ans, q = [], collections.deque() # 우선순위 큐?
        
        for a,b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1
        # print(graph,indegree,ans,q)
        
        # 진입차수 0인값 q에 append
        for n in range(numCourses):
            if indegree[n] == 0:
                q.append(n)
                
        while q:
            now = q.pop()
            ans.append(now)
            for i in graph[now]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    q.append(i)
        
        # 모든 강의를 들었으면, ans의 길이가 numCourses와 같기 때문에 ans를 리턴하고
        if len(ans) == numCourses:
            return ans
        # 아닌 경우 빈 list를 리턴한다.
        else:
            return []
        