# INSTRUCTOR: TO PREPARE:
#  - add test cases to class AllTests. They must begin with "test", and if it's
#    an extra credit test, it must begin with "test_extra_credit".
# 
#  - name all required definitions in REQUIRED_DEFNS.
# 
# to run on either a single file or all .py files in a folder (recursively):
#   python3 <thisfile.py> <your_one_file.py>
#   python3 <thisfile.py> <dir_of_files>

import unittest
import shutil
import sys
import os
import time

import importlib

############################################################################
############################################################################
# BEGIN SPECIALIZATION SECTION (the only part you need to modify beyond 
# adding new test cases).

# name all expected definitions; if present, their definition (with correct
# number of arguments) will be used; if not, a decoy complainer function
# will be used, and all tests on that function should fail.
	
REQUIRED_DEFNS = ["location",
				  "fibonacci",
				  "int_sqrt",
				  "sum_evens_2d"
				 ]

RENAMED_FILE = "student"

# END SPECIALIZATION SECTION
############################################################################
############################################################################



# enter batch mode by giving a directory to work on.
BATCH_MODE = (sys.argv[1] in ["."] or os.path.isdir(sys.argv[1]))

# This class contains multiple "unit tests" that each check
# various inputs to specific functions, checking that we get
# the correct behavior (output value) from completing the call.
class AllTests (unittest.TestCase):
	def test_loc1 (self): self.assertEqual (location([5,10,15,20,25],15),2)
	def test_loc2 (self): self.assertEqual (location([3,4,5,6,4,4,4,4,4],4),1)
	def test_loc3 (self): self.assertEqual (location([100, 105, 110],234),None)
	def test_loc4 (self): self.assertEqual (location([5,10,15,20,25],5),0)
	def test_loc5 (self): self.assertEqual (location([5,10,15,20,25],25),4)
	def test_loc6 (self): self.assertEqual (location([],5),None)
	def test_loc7 (self): self.assertEqual (location([2,3],3),1)
	def test_loc8 (self): self.assertEqual (location([3],3),0)
	def test_loc9 (self): self.assertEqual (location(["where","is","waldo","?"],"waldo"),2)
	def test_loc10(self): self.assertEqual (location([1,2,3,[2,3],4,5],[2,3]),3)
	
	def test_fib1 (self): self.assertEqual (fibonacci(0),1)
	def test_fib2 (self): self.assertEqual (fibonacci(1),1)
	def test_fib3 (self): self.assertEqual (fibonacci(2),2)
	def test_fib4 (self): self.assertEqual (fibonacci(3),3)
	def test_fib5 (self): self.assertEqual (fibonacci(4),5)
	def test_fib6 (self): self.assertEqual (fibonacci(5),8)
	def test_fib7 (self): self.assertEqual (fibonacci(7),21)
	def test_fib8 (self): self.assertEqual (fibonacci(15),987)
	def test_fib9 (self): self.assertEqual (fibonacci(100),573147844013817084101)
	def test_fib10(self): self.assertEqual (fibonacci(1000),70330367711422815821835254877183549770181269836358732742604905087154537118196933579742249494562611733487750449241765991088186363265450223647106012053374121273867339111198139373125598767690091902245245323403501)
	
	def test_int_sqrt1  (self): self.assertEqual (int_sqrt(1),1)
	def test_int_sqrt2  (self): self.assertEqual (int_sqrt(4),2)
	def test_int_sqrt3  (self): self.assertEqual (int_sqrt(5),2)
	def test_int_sqrt4  (self): self.assertEqual (int_sqrt(6),2)
	def test_int_sqrt5  (self): self.assertEqual (int_sqrt(7),2)
	def test_int_sqrt6  (self): self.assertEqual (int_sqrt(8),2)
	def test_int_sqrt7  (self): self.assertEqual (int_sqrt(9),3)
	def test_int_sqrt8  (self): self.assertEqual (int_sqrt(10000),100)
	def test_int_sqrt9  (self): self.assertEqual (int_sqrt(123456789),11111)
	def test_int_sqrt10 (self): self.assertEqual (int_sqrt(42),6)
	
	def test_sum_evens_2d_1 (self): self.assertEqual (sum_evens_2d([[1,2,3],[4,5,6]]),12)
	def test_sum_evens_2d_2 (self): self.assertEqual (sum_evens_2d([[1,2],[3,4],[5,6]]),12)
	def test_sum_evens_2d_3 (self): self.assertEqual (sum_evens_2d([[1,2,3,4,5,6]]),12)
	def test_sum_evens_2d_4 (self): self.assertEqual (sum_evens_2d([]),0)
	def test_sum_evens_2d_5 (self): self.assertEqual (sum_evens_2d([[]]),0)
	def test_sum_evens_2d_6 (self): self.assertEqual (sum_evens_2d([[120],[],[],[],[240]]),360)
	def test_sum_evens_2d_7 (self): self.assertEqual (sum_evens_2d([[1,3,5],[7,9,11]]),0)
	def test_sum_evens_2d_8 (self): self.assertEqual (sum_evens_2d([[1,2,3],[4,5],[6],[7,8,9]]),20)
	def test_sum_evens_2d_9 (self): self.assertEqual (sum_evens_2d([[-2,-3,-4,-5,-6],[-7,-8,-9,-10]]),-30)
	def test_sum_evens_2d_10(self): self.assertEqual (sum_evens_2d([[0,0,0,0,0],[0,0,0,0,0]]),0)

# This class digs through AllTests, counts and builds all the tests,
# so that we have an entire test suite that can be run as a group.
class TheTestSuite (unittest.TestSuite):
	# constructor.
	def __init__(self):
		# find all methods that begin with "test".
		fs = []
		for func in AllTests.__dict__:
			# append regular tests
			if str(func).startswith("test") and (not str(func).startswith("test_extra_credit")):
				fs.append(AllTests(str(func)))
			if str(func).startswith("test_extra_credit") and not BATCH_MODE:
				fs.append(AllTests(str(func)))
		
		# call parent class's constructor.
		unittest.TestSuite.__init__(self,fs)

class TheExtraCreditTestSuite (unittest.TestSuite):
		# constructor.
		def __init__(self):
			# find all methods that begin with "test".
			fs = []
			for func in AllTests.__dict__:
				if BATCH_MODE and str(func).startswith("test_extra_credit"):
					fs.append(AllTests(str(func)))
		
			# call parent class's constructor.
			unittest.TestSuite.__init__(self,fs)

# all (non-directory) file names, regardless of folder depth,
# under the given directory 'dir'.
def files_list(dir):
	info = os.walk(dir)
	filenames = []
	for (dirpath,dirnames,filez) in info:
#		print(dirpath,dirnames,filez)
		if dirpath==".":
			continue
		for file in filez:
			filenames.append(os.path.join(dirpath,file))
#		print(dirpath,dirnames,filez,"\n")
#		filenames.extend(os.path.join(dirpath, filez))
	return filenames

def main():
	if len(sys.argv)<2:
		raise Exception("needed student's file name as command-line argument:"\
			+"\n\t\"python3 tester4L.py gmason76_2xx_L4.py\"")
	
	if not BATCH_MODE:
		run_file(sys.argv[1])
	else:
		filenames = files_list(sys.argv[1])
	
# 		print(filenames)
	
		results = []
		for filename in filenames:
			try:
				print("\n\n\nRUNNING: "+filename)
				(tag, passed,tried,ec) = run_file(filename)
				results.append((tag,passed,tried,ec))
			except SyntaxError as e:
				results.append((filename+"_SYNTAX_ERROR",0,1))	
			except ValueError as e:
				return (filename+"_VALUE_ERROR",0,1)
			except TypeError as e:
				return (filename+"_TYPE_ERROR",0,1)
			except ImportError as e:
				results.append((filename+"_IMPORT_ERROR_TRY_AGAIN	",0,1))	
			except Exception as e:
				return (filename+str(e.__reduce__()[0]),0,1)
			
		print("\n\n\nGRAND RESULTS:\n")
		for (tag, passed, tried, ec) in results:
			print(("%.0f%%  (%d/%d, %dEC) - " % (passed/tried*100 + ec, passed, tried, ec))+tag)

# this will group all the tests together, prepare them as 
# a test suite, and run them.
def run_file(filename):

	# move the student's code to a valid file.
	shutil.copyfile(filename,"student.py")
	# wait half a second for file I/O to catch up...
		
	# import student's code, and *only* copy over the expected functions
	# for later use.
	import imp
	count = 0
	while True:
		try:
			import student
			imp.reload(student)
			break
		except ImportError as e:
			print("import error getting student.. trying again. "+os.getcwd(), os.path.exists("student.py"))
			time.sleep(0.5)
			count+=1
			if count>3:
				raise ImportError("too many attempts at importing!")
		except SyntaxError as e:
			results.append((filename+"_SYNTAX_ERROR",0,1))	
		except ValueError as e:
			return (filename+"_VALUE_ERROR",0,1)
		except TypeError as e:
			return (filename+"_TYPE_ERROR",0,1)
		except ImportError as e:
			results.append((filename+"_IMPORT_ERROR_TRY_AGAIN	",0,1))	
		except Exception as e:
			return (filename+str(e.__reduce__()[0]),0,1)
		except Exception as e:
			print("didn't get to import student yet... " + e)
	# but we want to re-load this between student runs...
	# the imp module helps us force this reload.s
	
	import student
	imp.reload(student)
	
	# make a global for each expected definition.
	def decoy(name):
		return (lambda x: "<no '%s' definition found>" % name)
		
	for fn in REQUIRED_DEFNS:
		globals()[fn] = decoy(fn)
		try:
			globals()[fn] = getattr(student,fn)
		except:
			print("\nNO DEFINITION FOR '%s'." % fn)	
	
	# create an object that can run tests.
	runner1 = unittest.TextTestRunner()
	
	# define the suite of tests that should be run.
	suite1 = TheTestSuite()
	
	# let the runner run the suite of tests.
	ans = runner1.run(suite1)
	num_errors   = len(ans.__dict__['errors'])
	num_failures = len(ans.__dict__['failures'])
	num_tests    = ans.__dict__['testsRun']
	num_passed   = num_tests - num_errors - num_failures
	# print(ans)
	
	
	if BATCH_MODE:
		# do the same for the extra credit.
		runnerEC = unittest.TextTestRunner()
		suiteEC = TheExtraCreditTestSuite()
		ansEC = runnerEC.run(suiteEC)
		num_errorsEC   = len(ansEC.__dict__['errors'])
		num_failuresEC = len(ansEC.__dict__['failures'])
		num_testsEC    = ansEC.__dict__['testsRun']
		num_passedEC   = num_testsEC - num_errorsEC - num_failuresEC
		print(ansEC)
	else:
		num_passedEC = 0
	
	# remove our temporary file.
	os.remove("student.py")
	if os.path.exists("__pycache__"):
		shutil.rmtree("__pycache__")
	
	tag = ".".join(filename.split(".")[:-1])
	return (tag, num_passed, num_tests,num_passedEC)

# this determines if we were imported (not __main__) or not;
# when we are the one file being run, perform the tests! :)
if __name__ == "__main__":
	main()
