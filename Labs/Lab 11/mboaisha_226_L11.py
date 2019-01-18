## Name: Mohammad BoAisha
## Lab Sec: 226
## Lab 11
## Collab: Alone


#XOXOXOXOXXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXO
#XOXOXOXOXXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXO
class Grade:
    def __init__(self, kind, name, percent):
        temp_list = ["test","lab","project","final"]
        if kind not in temp_list:
            print("Grading error exp goes here")
        else:
            self.kind = str(kind)
            self.name = str(name)
            self.percent = int(percent)
            
        def __str__(self):
            built_str = "{0}:{1}({2})".format(kind,name,percent)
            return built_str
        def __repr__(self):
            built_repr = "Grade('{0}', '{1}', {2})".format(kind,name,percent)
            return built_repr
        def __eq__(self,other):
            return self.kind==other.kind and self.name==other.name and self.percent==other.percent
#XOXOXOXOXXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXO
#XOXOXOXOXXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXO
class Gradebook:
	def __init__(self):
		pass
	def __str__(self):
		pass
	def add_grade(self, grade):
		pass
	def average_by_kind(self, kind):
		pass
	def get_all_of(self, kind):
		pass
	def get_by_name(self, name):
		pass
#XOXOXOXOXXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXO
#XOXOXOXOXXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXO
class GradingError(Exception):
	def __init__(self, msg):
		pass
	def __str__(self):
		pass
	def __repr__(self):
		pass