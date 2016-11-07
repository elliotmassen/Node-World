from sys import argv
from node import Node
from world import World
import time

script_name, initial_strength, max_mutation, max_nodes = argv
initial_strength = int(initial_strength)
max_mutation = int(max_mutation)
max_nodes = int(max_nodes)

world = World()
world.add(Node(initial_strength, max_mutation, world))

i = 0
while world.size() < max_nodes and world.nodes_are_alive():
	print "\nROUND " + str(i) + ":"
	world.print_stats()

	for n in world.nodes():
		n.heartbeat()

	i += 1
	time.sleep(0.5)

print "\nFINAL ROUND:"
world.print_stats()
print ""