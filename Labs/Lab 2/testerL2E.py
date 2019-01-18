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
	
REQUIRED_DEFNS = ["is_even","letter_grade","sum2biggest"]

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
	
	def test_even(self): self.assertEqual(is_even(5),False)
	def test_even(self): self.assertEqual(is_even(102),True)
	def test_even(self): self.assertEqual(is_even(-3),False)
	def test_even(self): self.assertEqual(is_even(0),True)
	
	def test_letter_grade1(self): self.assertEqual(letter_grade(105),"A+")
	def test_letter_grade2(self): self.assertEqual(letter_grade(100),"A+")
	def test_letter_grade3(self): self.assertEqual(letter_grade(98),"A+")
	def test_letter_grade4(self): self.assertEqual(letter_grade(97),"A")
	def test_letter_grade5(self): self.assertEqual(letter_grade(92),"A")
	def test_letter_grade6(self): self.assertEqual(letter_grade(91),"A-")
	def test_letter_grade7(self): self.assertEqual(letter_grade(90),"A-")
	def test_letter_grade8(self): self.assertEqual(letter_grade(89),"B+")
	def test_letter_grade9(self): self.assertEqual(letter_grade(88),"B+")
	def test_letter_grade10(self): self.assertEqual(letter_grade(87),"B")
	def test_letter_grade11(self): self.assertEqual(letter_grade(85),"B")
	def test_letter_grade12(self): self.assertEqual(letter_grade(82),"B")
	def test_letter_grade13(self): self.assertEqual(letter_grade(81),"B-")
	def test_letter_grade14(self): self.assertEqual(letter_grade(80),"B-")
	def test_letter_grade15(self): self.assertEqual(letter_grade(79),"C+")
	def test_letter_grade16(self): self.assertEqual(letter_grade(78),"C+")
	def test_letter_grade17(self): self.assertEqual(letter_grade(76),"C")
	def test_letter_grade18(self): self.assertEqual(letter_grade(73),"C")
	def test_letter_grade19(self): self.assertEqual(letter_grade(72),"C")
	def test_letter_grade20(self): self.assertEqual(letter_grade(71),"C-")
	def test_letter_grade21(self): self.assertEqual(letter_grade(70),"C-")
	def test_letter_grade22(self): self.assertEqual(letter_grade(69),"D")
	def test_letter_grade23(self): self.assertEqual(letter_grade(68),"D")
	def test_letter_grade24(self): self.assertEqual(letter_grade(65),"D")
	def test_letter_grade25(self): self.assertEqual(letter_grade(61),"D")
	def test_letter_grade26(self): self.assertEqual(letter_grade(60),"D")
	def test_letter_grade27(self): self.assertEqual(letter_grade(59),"F")
	def test_letter_grade28(self): self.assertEqual(letter_grade(30),"F")
	def test_letter_grade29(self): self.assertEqual(letter_grade(0),"F")
 	
	def test_sum2biggest1(self): self.assertEqual(sum2biggest(5,3,4),9)
	def test_sum2biggest2(self): self.assertEqual(sum2biggest(-5,-3,-1),-4)
	def test_sum2biggest3(self): self.assertEqual(sum2biggest(6,4,6),12)
	def test_sum2biggest4(self): self.assertEqual(sum2biggest(0,0,0),0)
	def test_sum2biggest5(self): self.assertEqual(sum2biggest(2,3,4),7)
	def test_sum2biggest6(self): self.assertEqual(sum2biggest(2,4,3),7)
	def test_sum2biggest7(self): self.assertEqual(sum2biggest(3,2,4),7)
	def test_sum2biggest8(self): self.assertEqual(sum2biggest(3,4,2),7)
	def test_sum2biggest9(self): self.assertEqual(sum2biggest(4,2,3),7)
	def test_sum2biggest10(self): self.assertEqual(sum2biggest(4,3,2),7)
	def test_sum2biggest11(self): self.assertEqual(sum2biggest(3,3,7),10)
	def test_sum2biggest12(self): self.assertEqual(sum2biggest(3,7,3),10)
	def test_sum2biggest13(self): self.assertEqual(sum2biggest(7,3,3),10)
	def test_sum2biggest14(self): self.assertEqual(sum2biggest(5,8,8),16)
	def test_sum2biggest15(self): self.assertEqual(sum2biggest(8,5,8),16)
	def test_sum2biggest16(self): self.assertEqual(sum2biggest(8,8,5),16)
	def test_sum2biggest17(self): self.assertEqual(sum2biggest(-5,-5,-3),-8)
	def test_sum2biggest18(self): self.assertEqual(sum2biggest(-6,-4,-4),-8)
	def test_sum2biggest19(self): self.assertEqual(sum2biggest(-5,0,3),3)
	def test_sum2biggest20(self): self.assertEqual(sum2biggest(-10,-5,5),0)

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
			+"\n\t\"python3 tester_lab3e.py gmason76_2B5_L3.py\"")
	
	
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
