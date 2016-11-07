from sys import argv
from node import Node
import time

script_name, initial_strength, max_mutation, max_nodes = argv
initial_strength = int(initial_strength)
max_mutation = int(max_mutation)
max_nodes = int(max_nodes)

def print_stats():
	print "Total nodes: " + str(world.size()) + " | Dead nodes: " + str(world.dead_nodes()) + " | Surviving nodes: " + str(100 - (float(world.dead_nodes()) / float(world.size())) * 100) + "%"
	print "MAX LIFE: " + str(world.get_max_life())

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
		while i < world.size() and not alive:
			if self.__nodes[i].get_life() > 0:
				alive = True
			i += 1

		return alive

	def add_grave(self):
		self.__graveyard += 1

	def dead_nodes(self):
		return self.__graveyard

world = World()
world.add(Node(initial_strength, max_mutation, world))

i = 0
while world.size() < max_nodes and world.nodes_are_alive():
	print "\nROUND " + str(i) + ":"
	print_stats()

	for n in world.nodes():
		n.heartbeat()

	i += 1
	time.sleep(0.5)

print "\nFINAL ROUND:"
print_stats()
print ""