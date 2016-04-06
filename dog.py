#defines the data that a dog contains
class Dog:
	def __init__(self, name, color, dam=None, sire=None):
		self.name = name
		self.dam = dam
		self.color = color
		self.sire = sire

	def __str__(self):
		return str(self.name) + ": " + str(self.color) + ", [sire: " + str(self.sire) + ", dam: " + str(self.dam)+"]"

	def preorder(self, node):
		if node:
			print node
			self.preorder(node.dam)
			self.preorder(node.sire)

	def postorder(self, node):
		if node:
			self.postorder(node.dam)
			self.postorder(node.sire)
			print node
