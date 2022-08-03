# class Solution:
#     def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
#         '''
#         prerequisites[i] =  [a, b]   -> a를 듣기 위해서는 반드시 b를 들어야 한다. 
#         모든 코스를 
#         '''
#         # 위상정렬 - 189ms
#         graph = collections.defaultdict(list) # 그래프 초기화
#         indegree = [0] * numCourses # 진입차수 초기화 
#         ans, q = [], collections.deque() # 우선순위 큐?
        
#         for a,b in prerequisites:
#             graph[b].append(a)
#             indegree[a] += 1
#         # print(graph,indegree,ans,q)
        
#         # 진입차수 0인값 q에 append
#         for n in range(numCourses):
#             if indegree[n] == 0:
#                 q.append(n)
                
#         while q:
#             now = q.pop()
#             ans.append(now)
#             for i in graph[now]:
#                 indegree[i] -= 1
#                 if indegree[i] == 0:
#                     q.append(i)
        
#         # 모든 강의를 들었으면, ans의 길이가 numCourses와 같기 때문에 ans를 리턴하고
#         if len(ans) == numCourses:
#             return ans
#         # 아닌 경우 빈 list를 리턴한다.
#         else:
#             return []

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Create a prerequisite dict. (containing courses (nodes) that need to be taken (visited)
		# before we can visit the key.
        preq = {i:set() for i in range(numCourses)}
		# Create a graph for adjacency and traversing.
        graph = collections.defaultdict(set)
        for i,j in prerequisites:
		    # Preqs store requirments as their given.
            preq[i].add(j)
			# Graph stores nodes and neighbors.
            graph[j].add(i)
        
        q = collections.deque([])
		# We need to find a starting location, aka courses that have no prereqs.
        for k, v in preq.items():
            if len(v) == 0:
                q.append(k)
		# Keep track of which courses have been taken.
        taken = []
        while q:
            course = q.popleft()
            taken.append(course)
			# If we have visited the numCourses we're done.
            if len(taken) == numCourses:
                return taken
			# For neighboring courses.
            for cor in graph[course]:
			    # If the course we've just taken was a prereq for the next course, remove it from its prereqs.
                preq[cor].remove(course)
				# If we've taken all of the preqs for the new course, we'll visit it.
                if not preq[cor]:
                    q.append(cor)
		# If we didn't hit numCourses in our search we know we can't take all of the courses.
        return []        