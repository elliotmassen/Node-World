class World():
	def __init__(self):
		self.__nodes = []
		self.__max_life = 0
		self.__graveyard = 0

	def add(self, node):
		self.__nodes.append(node)

		if node.get_life() > self.__max_life:
			self.__max_life = node.get_life()

	def size(self):
		return len(self.__nodes)

	def nodes(self):
		return self.__nodes

	def get_max_life(self):
		return self.__max_life

	def nodes_are_alive(self):
		alive = False
		i = 0
		while i < self.size() and not alive:
			if self.__nodes[i].get_life() > 0:
				alive = True
			i += 1

		return alive

	def add_grave(self):
		self.__graveyard += 1

	def dead_nodes(self):
		return self.__graveyard

	def print_stats(self):
		print "Total nodes: " + str(self.size()) + " | Dead nodes: " + str(self.dead_nodes()) + " | Surviving nodes: " + str(100 - (float(self.dead_nodes()) / float(self.size())) * 100) + "%"
		print "MAX LIFE: " + str(self.get_max_life())