def constructTree(sample, segmentTree, low, high, pos):
	print("Here")
	if low == high:
		segmentTree[pos] = sample[low]
		return None
  	
	mid = (low + high)/2
	constructTree(sample,segmentTree, low, mid, 2*pos+1)
	constructTree(sample,segmentTree, mid+1, high, 2*pos+1)
	segmentTree[pos] = min(segmentTree[2*pos+1], segmentTree[2*pos+2])

sample = [-1,2,4,0]
twoPowerRange = len(sample)

for i in range(twoPowerRange):
	if(2**i >= twoPowerRange):
		segmentTreeLength = 2**i * 2 - 1
		print(segmentTreeLength)
		break
	
maxValue = max(sample) + 1
segmentTree = []
while len(segmentTree) <segmentTreeLength:
  segmentTree.append(maxValue)

constructTree(sample, segmentTree, 0, twoPowerRange-1, 0)
print(segmentTree)

# https://www.youtube.com/watch?v=ZBHKZF5w4YU&t=1299s - 21:11