############################################################################################################################################
############################################################################################################################################
#
#	CDFG MANAGER
#
############################################################################################################################################
#	FUNCTIONS:
#				- get_cdfg_edges : retrieve edges of cdfg
#				- get_cdfg_nodes : retrieve nodes of cdfg
#				- update_dic_list : update the value of a key (where the value is a list)
#				- create_control_edge : create a control edge between src and dst in the cdfg
#				- is_control_edge : check if edge between src and dst is a control edge
############################################################################################################################################
############################################################################################################################################


# function to retrieve edges of cdfg
def get_cdfg_edges(cdfg):
	return map(lambda e : cdfg.get_edge(*e), cdfg.edges(keys=True))

# function to retrieve nodes of cdfg
def get_cdfg_nodes(cdfg):
	return map(lambda n : cdfg.get_node(n), cdfg.nodes())

# function to update the value of a key (where the value is a list)
def update_dic_list(dic, key, new_element):
	if key in dic:
		inst_list = dic[key]
	else:
		inst_list = []
	inst_list.append(new_element)
	dic[key] = inst_list
	return dic

# function to create a control edge between src and dst in the cdfg
def create_control_edge(cdfg, src, dst):
	cdfg.add_edge(src, dst, style="dashed")
	return cdfg

# function to check if edge between src and dst is a control edge
def is_control_edge(cdfg, src, dst):
	pass


''' assume that the input graph is a DAG, return topological ordering among the nodes
	https://en.wikipedia.org/wiki/Topological_sorting#Depth-first_search '''

def get_topological_order(cdfg):
	print(type(cdfg))
	# node_list: historical ordering
	# temp_list: a DFS run
	node_list, temp_list = [], []
	def visit(node):
		if node in node_list:
			return
		assert node not in temp_list, 'error - the CDFG graph still has at least one cycle!'
		temp_list.append(node)
		for e in get_cdfg_edges(cdfg):
			# skip to visit the dashed edges: they are for sure cyclic
			if e[0] == node and not ('style' in e.attr and e.attr['style'] == 'dashed'): 
				visit(e[1])
		node_list.insert(0, node)
		temp_list.remove(node)
	
	# we call a separate DFS per each node
	for node in get_cdfg_nodes(cdfg): 
		if node not in node_list:
			visit(node)
	
	return node_list
