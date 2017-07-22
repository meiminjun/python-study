class Student(object):
	"""docstring for Student"""
	def __init__(self, name, age):
		super(Student, self).__init__()
		self.name = name
		self.age = age


bart = Student('Bart Simpson', 59)
xiao = Student('meiminjun', 26)
print(bart.name)
print(xiao.age)
