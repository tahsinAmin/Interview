#  Segment Tree Range Minimum Query =  https://www.youtube.com/watch?v=ZBHKZF5w4YU&t=1036s
def constructTree(sample, segmentTree, low, high, pos):
	if low == high:
		segmentTree[pos] = sample[low]
		return None
  	
	mid = (low + high)//2
	constructTree(sample,segmentTree, low, mid, 2*pos+1)
	constructTree(sample,segmentTree, mid+1, high, 2*pos+2)
	segmentTree[pos] = min(segmentTree[2*pos+1], segmentTree[2*pos+2])

def rangeMinQuery( segmentTree, qLow, qHigh, low, high, pos):
	if(qLow <= low and qHigh >= high): # total overlap
		return segmentTree[pos]
	if(qLow > high or qHigh < low): # no overlap
		return 10 # a random MAX_VALUE for now
	mid = (low+high)/2
	return min(
		rangeMinQuery(segmentTree, qLow, qHigh, low, mid, 2*pos+1),
		rangeMinQuery(segmentTree, qLow, qHigh, mid+1, high, 2*pos+2)
		)

sample = [-1,2,4,0]
twoPowerRange = len(sample)

for i in range(twoPowerRange):
	if(2**i >= twoPowerRange):
		segmentTreeLength = 2**i * 2 - 1
		break
	
maxValue = max(sample) + 1
segmentTree = []
while len(segmentTree) < segmentTreeLength:
  segmentTree.append(maxValue)

constructTree(sample, segmentTree, 0, twoPowerRange-1, 0)
print(segmentTree)

# Here we gave the the range  1 to 3 in 2nd and 3rd paramenter. Change it whatever way you like
min_value_in_range = rangeMinQuery(segmentTree, 1, 3, 0, twoPowerRange-1, 0)
print(min_value_in_range)