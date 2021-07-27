def find_set_representative(parentGraph, node):
	if(parentGraph[node] < 0):
		return node		
	else:
		representative_node = find_set_representative(parentGraph, parentGraph[node])
		parentGraph[node] = representative_node
		return representative_node

def in_same_set(parentGraph, m, n):
	if m is n:
		return True
	elif parentGraph[m] is -1:
		return False
	return in_same_set(parentGraph, parentGraph[m], n)

def union(parentGraph, m, n):
	mRoot =  find_set_representative(parentGraph, m)
	nRoot =  find_set_representative(parentGraph, n)

	if mRoot == nRoot:
		return False
	else:
		if parentGraph[mRoot] == parentGraph[nRoot]:
			parentGraph[mRoot] = parentGraph[mRoot] + parentGraph[nRoot]
			parentGraph[nRoot] = mRoot
		else:
			if parentGraph[mRoot] < parentGraph[nRoot]:
				parentGraph[mRoot] = parentGraph[nRoot] + parentGraph[mRoot]
				parentGraph[nRoot] = mRoot
			else:
				parentGraph[nRoot] = parentGraph[nRoot] + parentGraph[mRoot]
				parentGraph[mRoot] = nRoot

n = 7
parentGraph = {}

for i in range(n):
	parentGraph[i] = -1
	
ipt = [[0,1], [1,2], [2,3], [4,5]]
print(parentGraph)

for m,n in ipt:
	union(parentGraph, m,n)
	print(parentGraph)
	
print(parentGraph)

print(find_set_representative(parentGraph,1))
print(find_set_representative(parentGraph,0))
union(parentGraph, 4,2)

print(parentGraph)

# https://www.youtube.com/watch?v=WQbbFhPGBN0
# 23:44