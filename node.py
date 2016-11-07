from random import randint

class Node():
	def __init__(self, life, max_mutation, world):
		self.__life = life
		self.max_mutation = max_mutation
		self.__world = world

	def __mutate(self):
		return self.__life * randint(0, self.max_mutation)

	def split(self):
		self.__life /= 2
		mutation = self.__mutate()
		self.__world.add(Node(mutation, self.max_mutation, self.__world))

	def heartbeat(self):
		if self.__life < 0:
			pass
		if self.__life == 0:
			self.__world.add_grave()
			self.__life = -1
		else:
			if(self.__life > 0):
				self.__life -= 1

			if(self.__life > 2):
				self.split()

	def get_life(self):
		return self.__life