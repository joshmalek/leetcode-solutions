# Link: https://leetcode.com/problems/clone-graph/submissions/

#OPTIMIZED VERSION
def cloneGraph(self, node: 'Node') -> 'Node':
    if(node == None):
        return node
    q = collections.deque()
    q.append(node)
    visited = dict()
    visited[node.val] = Node(node.val)
    while(q):
        curr_node = q.popleft()
        for n in curr_node.neighbors:
            if(n.val not in visited):
                visited[n.val] = Node(n.val)
                q.append(n)
            visited[curr_node.val].neighbors.append(visited[n.val])
    return visited[node.val]

# UNOPTIMIZED VERSION
# def cloneGraph(self, node: 'Node') -> 'Node':
#     if(node == None):
#         return node
#     if(len(node.neighbors)==0):
#         return Node(node.val)
#     q = collections.deque()
#     q.append(node)
#     visited = dict()

#     while(q):
#         curr_node = q.popleft()
#         print("visited node ", curr_node.val)
#         visited[curr_node] = Node(curr_node.val)
#         for n in curr_node.neighbors:
#             if(n not in visited):
#                 visited[n] = Node(n.val)
#                 q.append(n)
#     #for each node in the dictionary
#     for n in visited:
#         # for each neighbor for each node
#         for nbs in n.neighbors:
#             #the copy gets all the neighbors appended
#             visited[n].neighbors.append(visited[nbs])
#     #return the copied root node
#     for i in visited[node].neighbors:
#         print(i.val)
#     return visited[node]