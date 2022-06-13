#edge is given as [starting verrtex, ending vertex, weight]

def kruskalnodes(tree):

	num_of_edges_in_tree = len(tree)
	num_of_edges_in_minspantree = num_of_edges_in_tree - 1

	#sorting on basis of weight
	tree.sort(key = lambda x : x[2])

	minspantree.append(tree[0])
	for i in tree:
		minspantree.append(i)
		checkcycle(minspantree)
	return minspantree

def checkcycle(tree):
	#if no cycle then return as it is otherwise pop last element and return
