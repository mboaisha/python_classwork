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
	
REQUIRED_DEFNS = ["odd_product",
				  "divisors",
				  "has_duplicates",
				  "truncatable_prime",
				  "histogram",
				  "second_smallest",
				  "mode"
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
	def test_odd_product1  (self): self.assertEqual (odd_product([1,2,3,4,5]), 15)
	def test_odd_product2  (self): self.assertEqual (odd_product([2,4,6]),1)
	def test_odd_product3  (self): self.assertEqual (odd_product([]), 1)
	def test_odd_product4  (self): self.assertEqual (odd_product([5]), 5)
	def test_odd_product5  (self): self.assertEqual (odd_product([8]), 1)
	def test_odd_product6  (self): self.assertEqual (odd_product([2,4,3,5,8]), 15)
	def test_odd_product7  (self): self.assertEqual (odd_product([-3]), -3)
	def test_odd_product8  (self): self.assertEqual (odd_product([-3,-2,-1,0,1,2,3]), 9)
	def test_odd_product9  (self): self.assertEqual (odd_product([0,1,2,3,4,5]), 15)
	def test_odd_product10 (self): self.assertEqual (odd_product([1,2,3,4,5,0]), 15)
	def test_odd_product11 (self): self.assertEqual (odd_product([0,0,0]),1)
	def test_odd_product12_dont_modify_list (self):
		xs = [1,3,5,7,6,4,2,8,7,6,5,4,3,2,1]
		
		# a complete copy
		orig = xs[:] 
		
		ans = odd_product(xs)
		
		# must still get right answer
		self.assertEqual (ans, 11025)
		
		# must not have changed the original list
		self.assertTrue (xs==orig) 
	
	def test_divisors1  (self): self.assertEqual (divisors(12),[1,2,3,4,6,12])
	def test_divisors2  (self): self.assertEqual (divisors(13),[1,13])
	def test_divisors3  (self): self.assertEqual (divisors(1),[1])
	def test_divisors4  (self): self.assertEqual (divisors(1111181),[1,1111181]) # prime!
	def test_divisors5  (self): self.assertEqual (divisors(40),[1, 2, 4, 5, 8, 10, 20, 40])
	def test_divisors6  (self): self.assertEqual (divisors(9),[1,3,9])
	def test_divisors7  (self): self.assertEqual (divisors(11*13),[1,11,13,143])
	def test_divisors8  (self): self.assertEqual (divisors(144),[1,2,3,4,6,8,9,12,16,18,24,36,48,72,144])
	def test_divisors9  (self): self.assertEqual (divisors(999),[1,3,9,27,37,111,333,999])
	def test_divisors10 (self): self.assertEqual (divisors(1000),[1,2,4,5,8,10,20,25,40,50,100,125,200,250,500,1000])
	def test_divisors11 (self): self.assertEqual (divisors(42),[1,2,3,6,7,14,21,42])
	def test_divisors12 (self): self.assertEqual (divisors(81),[1,3,9,27,81])
	
	def test_has_duplicates1  (self): self.assertEqual (has_duplicates("meter"),True)
	def test_has_duplicates2  (self): self.assertEqual (has_duplicates([]),False)
	def test_has_duplicates3  (self): self.assertEqual (has_duplicates([1]),False)
	def test_has_duplicates4  (self): self.assertEqual (has_duplicates([1,1]),True)
	def test_has_duplicates5  (self): self.assertEqual (has_duplicates([1,3,5,2,4]),False)
	def test_has_duplicates6  (self): self.assertEqual (has_duplicates([1,1,2,3,5]),True)
	def test_has_duplicates7  (self): self.assertEqual (has_duplicates([5,10,15,5,20]),True)
	def test_has_duplicates8  (self): self.assertEqual (has_duplicates([5,10,15,20,5]),True)
	def test_has_duplicates9  (self): self.assertEqual (has_duplicates([1,2,3,4,4,5]),True)
	def test_has_duplicates10 (self): self.assertEqual (has_duplicates([[1,2],[1,3],[2,3]]),False)
	def test_has_duplicates11 (self): self.assertEqual (has_duplicates([[1,2],[2,3],[3,4],[3,4]]),True)
	def test_has_duplicates12 (self): self.assertEqual (has_duplicates("hello"),True)
	def test_has_duplicates13 (self): self.assertEqual (has_duplicates("wordWORD \t"),False)
	def test_has_duplicates14 (self): self.assertEqual (has_duplicates('msg:"\"'),True)
	def test_has_duplicates15_dont_modify_list (self):
		xs = [1,3,5,7,6,4,2,8,7,6,5,4,3,2,1]
		
		# a complete copy
		orig = xs[:] 
		
		ans = has_duplicates(xs)
		
		# must still get right answer
		self.assertTrue (ans)
		
		# must not have changed the original list
		self.assertTrue (xs==orig) 
	
	def test_truncatable_prime1  (self): self.assertEqual (truncatable_prime(2),True)
	def test_truncatable_prime2  (self): self.assertEqual (truncatable_prime(113),False)
	def test_truncatable_prime3  (self): self.assertEqual (truncatable_prime(5939),True)
	def test_truncatable_prime4  (self): self.assertEqual (truncatable_prime(53),True)
	def test_truncatable_prime5  (self): self.assertEqual (truncatable_prime(2357),False)
	def test_truncatable_prime6  (self): self.assertEqual (truncatable_prime(23),True)
	def test_truncatable_prime7  (self): self.assertEqual (truncatable_prime(7393),True)
	def test_truncatable_prime8  (self): self.assertEqual (truncatable_prime(7391),False)
	def test_truncatable_prime9  (self): self.assertEqual (truncatable_prime(73939),True)
	def test_truncatable_prime10 (self): self.assertEqual (truncatable_prime(1),False)
	def test_truncatable_prime11 (self): self.assertEqual (truncatable_prime(7532),False)
	def test_truncatable_prime12 (self): self.assertEqual (truncatable_prime(59),True)
	def test_truncatable_prime13 (self): self.assertEqual (truncatable_prime(5353),False)

	def test_histogram1  (self): self.assertEqual (histogram([3,10,0,5]),'ooo\noooooooooo\n\nooooo')
	def test_histogram2  (self): self.assertEqual (histogram([]),'')
	def test_histogram3  (self): self.assertEqual (histogram([0]),'')
	def test_histogram4  (self): self.assertEqual (histogram([1,2,3]),'o\noo\nooo')
	def test_histogram5  (self): self.assertEqual (histogram([5,0,0,0,3]),'ooooo\n\n\n\nooo')
	def test_histogram6  (self): self.assertEqual (histogram([9]),'ooooooooo')
	def test_histogram7  (self): self.assertEqual (histogram([1,2,1,1,3,1,1,1]),'o\noo\no\no\nooo\no\no\no')
	def test_histogram8  (self): self.assertEqual (histogram([46,30]),'oooooooooooooooooooooooooooooooooooooooooooooo\noooooooooooooooooooooooooooooo')
	def test_histogram9  (self): self.assertEqual (histogram([3,1,0]),'ooo\no\n')
	def test_histogram10 (self): self.assertEqual (histogram([100,99,101]),'oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo\nooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo\nooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo')
	def test_histogram11 (self): self.assertEqual (histogram([1,0,1,0,1,0]),'o\n\no\n\no\n')
	def test_histogram12 (self): self.assertEqual (histogram([1,1,1]),'o\no\no')
	def test_histogram13_dont_modify_list (self):
		xs = [1,3,5,7,6,4,2,8,7,6,5,4,3,2,1]
		
		# a complete copy
		orig = xs[:] 
		
		ans = histogram(xs)
		
		# must still get right answer
		self.assertEqual (ans, 'o\nooo\nooooo\nooooooo\noooooo\noooo\noo\noooooooo\nooooooo\noooooo\nooooo\noooo\nooo\noo\no')
		
		# must not have changed the original list
		self.assertTrue (xs==orig)
		
	def test_second_smallest1  (self): self.assertEqual (second_smallest([1,2,3,4,5]),2)
	def test_second_smallest2  (self): self.assertEqual (second_smallest([5,1,-4,-3,2]),-3)
	def test_second_smallest3  (self): self.assertEqual (second_smallest([2,4,3,2,5]),2)
	def test_second_smallest4  (self): self.assertEqual (second_smallest([1,1,2,3]),1)
	def test_second_smallest5  (self): self.assertEqual (second_smallest([7,8,7,9]),7)
	def test_second_smallest6  (self): self.assertEqual (second_smallest([3,4,5,3]),3)
	def test_second_smallest7  (self): self.assertEqual (second_smallest([3,2,2,4]),2)
	def test_second_smallest8  (self): self.assertEqual (second_smallest([4,3,5,3]),3)
	def test_second_smallest9  (self): self.assertEqual (second_smallest([5,4,3,2,1]),2)
	def test_second_smallest10 (self): self.assertEqual (second_smallest([5,3,4,2,3,1]),2)
	def test_second_smallest11 (self): self.assertEqual (second_smallest([5,4,2,1,3]),2)
	def test_second_smallest12 (self): self.assertEqual (second_smallest([7,7,7,7,7,7,7]),7)
	def test_second_smallest13 (self): self.assertEqual (second_smallest([3,5,2]),3)
	def test_second_smallest14 (self): self.assertEqual (second_smallest([3,5,4,2]),3)
	def test_second_smallest15_dont_modify_list (self):
		xs = [1,3,5,7,6,4,2,8,7,6,5,4,3,2,1]
		
		# a complete copy
		orig = xs[:] 
		
		ans = second_smallest(xs)
		
		# must still get right answer
		self.assertEqual (ans, 1)
		
		# must not have changed the original list
		self.assertTrue (xs==orig) 

	def test_extra_credit_mode1 (self): self.assertEqual (mode([1,5,2,5,4,5]),[5])
	def test_extra_credit_mode2 (self): self.assertEqual (mode([1,4,2,4,2,3]),[4,2])
	def test_extra_credit_mode3 (self): self.assertEqual (mode([1,2,3,4]),[1,2,3,4])
	def test_extra_credit_mode4 (self): self.assertEqual (mode([1,2,3,2,3,2,3,1,1,1]),[1])
	def test_extra_credit_mode5_dont_modify_list (self):
		xs = [1,3,5,7,6,4,2,8,7,6,5,4,3,2,1]
		
		# a complete copy
		orig = xs[:] 
		
		ans = mode(xs)
		
		# must still get right answer
		self.assertEqual (ans, [1,3,5,7,6,4,2])
		
		# must not have changed the original list
		self.assertTrue (xs==orig) 




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
