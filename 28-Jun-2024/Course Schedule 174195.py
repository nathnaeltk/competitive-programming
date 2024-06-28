# Problem: Course Schedule - https://leetcode.com/problems/course-schedule/

class Solution:
	def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
		graph=defaultdict(list)
		indegree={}

		for i in range(numCourses):
			indegree[i]=0	

		for child,parent in prerequisites:
			graph[parent].append(child)
			indegree[child]+=1

		queue=deque()
		for key,value in indegree.items():
			if value==0:
				queue.append(key)

		courseSequence=[]
		while queue:
			course=queue.popleft()
			courseSequence.append(course)
			for neighbour in graph[course]:
				indegree[neighbour]-=1
				if indegree[neighbour]==0:
					queue.append(neighbour)

		return len(courseSequence)==numCourses