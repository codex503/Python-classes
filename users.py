class Users():
	"""a simple exercise on how to access functions in classes"""
	def __init__(self,first,last):
		"""Initialize name attributes"""
		self.first = first
		self.last = last

	def describe_user(self):
		"""printing the user's info"""
		return self.first.title() + " " + self.last.title()
		
	def greet_user(self):
		 greet = "Hello! " + self.first.title() + " how are you today?"
		 return greet

derek = Users('James','Pinot')

print(derek.describe_user())
print(derek.greet_user())

