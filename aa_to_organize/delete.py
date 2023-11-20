# Creating a class
class A:

	# Declaring public method
	def fun(self):
		print("Public method")

	# Declaring private method
	def __fun(self):
		print("Private method")


# Driver's code
obj = A()

# Calling the private member
# through name mangling
obj._A__fun()
