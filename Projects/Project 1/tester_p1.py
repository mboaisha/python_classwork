################################################################################
# 
# NOTE TO STUDENTS:
# 
# you don't need to read through this file at all. Just run
# this OS-prompt command on your code:
# 
#     python3 tester_p1.py yourfilehere.py
#
# This file needs the corresponding tests.txt file to be in the
# same directory.
# 
# If you ever notice files named "student.py", "complaints.txt", or a folder 
# named "__pychache__", you can delete them. Make sure your own file stays 
# around, that's the one file you'll need to turn in, named similar to:
# 
# 		gmason76_230_P1.py
# 
# 
################################################################################

import sys
import os
import io
import shutil

import traceback


# how many #'s to draw as a visual breaker?
banner_width = 30

# try to ignore everything we can.
def sanitize(message):
	# lower-case everything.
	message = message.lower()
	
	# normalize whitespace. Students might struggle here if
	# they *didn't* include any!
	message = " ".join(message.split())
	# return what we've got.
	return message

# builds up one single test case.
class Test:
	def __init__(self, inputs, expected, complaintsfilename = "complaints.txt"):
		self.inputs = inputs
		self.expected = expected
		#self.complaintsfile = open(complaintsfile,"a")
		self.complaintsfilename = complaintsfilename
	
	# group together list of inputs from many lines into one string.
	def prep_inputs(self,xs):
		s = ""
		for x in xs:
			s += str(x)+"\n"
		return s
	
	# maybe not needed anymore; way to reset stdin/out.
	# They get reassigned below.
	def reset(self):
		sys.stdin = sys.__stdin__
		sys.stdout = sys.__stdout__
	
		
	# run an individual test case. use other files
	# for inputs/outputs/error messages.	
	def run(self, outfilename = "results.txt", lenient=False):
		self.complaintsfile = open(self.complaintsfilename,"a")
		answer = True
		try:
			# change stdin to a string(!)
			sys.stdin = io.StringIO(self.prep_inputs(self.inputs))
			sys.stdout = open(outfilename,"w")
			import student
			student.student_main()
			sys.stdout.close()
			got = open(outfilename).read()
			if lenient:
				got = sanitize(got)
				self.expected = sanitize(self.expected)
			if got!=self.expected:
				hard_print("E",end="")
				print(("#"*banner_width)+"\n"
				      +"failure:\n"
					  +"    fed these arguments: "+str(" ".join(self.inputs))
					  +"\n"
				      +"    expected:\n"
					  +'"""'+(repr(self.expected))
					  +'"""\n    got:\n'
					  +'"""'+(repr(got))+'"""\n'
					  ,file=self.complaintsfile
					  )
				answer = False
			else:
				hard_print(".",end="")
				answer = True
		# sometimes the files are read/written/closed too soon or late. 
		# rather than deal with these race conditions (meaning waiting for
		# the files to be read/written/closed), we just ask for 
		# a re-run in these few cases. Sorry.
		except ValueError as ve:
			if str(ve).startswith("I/O operation on closed file."):
				hard_print("OOPS! poor timing... please run tests file "
							+"again! (closed file issue)")
				sys.exit(1)
		except ImportError as ie:
			if str(ie).startswith("No module named 'student'"):
				hard_print("OOPS! poor timing... please run tests file "
							+"again! (imported before file was created)")
				sys.exit(1)
		except FileNotFoundError as e:
			if str(e).startswith("[Errno 2] No such file or directory:"
							+" 'complaints.txt'"):
				hard_print("OOPS! poor timing... please run tests file "
							+"again! (complaints.txt wasn't yet created)")
				sys.exit(1)
		# anything else that goes wrong is supposedly an
		# actual student-code failure.
		except Exception as e:
			hard_print("F",end="")
			print(("#"*banner_width)+"\n"
				 +"failure: ",type(e),e
				 , file=self.complaintsfile)
			traceback.print_exception(*sys.exc_info(),file=self.complaintsfile)
			answer = False
		self.reset()
		self.complaintsfile.close()
		return answer

# batch of Test values.
class Tests:
	def __init__(self):
		self.tests = []
	def add(self, test):
		self.tests.append(test)
	# run them all. can be done leniently (massaging string formatting/spacing
	# for better matching possibilities).
	def run(self, printout=True, lenient=False):
		# empty the complaints file.
		open("complaints.txt","w").close()
		count = 0
		for test in self.tests:
			if test.run(lenient=lenient):
				count+=1
		if printout:
			try:
				f = open("complaints.txt")
				s = f.read()
				if s!="":
					print("\n"+s)
				f.close()
				if os.path.exists("complaints.txt"):
					os.remove("complaints.txt")
			except FileNotFoundError as e:
				if str(e).startswith("[Errno 2] No such file or directory: 'complaints.txt'"):
					hard_print("OOPS! poor timing... please run tests file again! (complaints.txt wasn't yet created)")
					sys.exit(1)
		return (count,len(self.tests))

# dig through the files' INPUT/OUTPUT/ENDTESTS style.
def build_tests(filename):
	with open(filename) as f:
		lines = f.read().split("\n")
	tests = Tests()
	while len(lines)>0 and lines[0] =="INPUT":
		lines.pop(0) # drop "INPUT" line
		ins = []
		while len(lines)>0 and lines[0]!="OUTPUT":
			ins.append(lines.pop(0))
		if len(lines)>0:
			lines.pop(0) # drop "OUTPUT" line
		outs = []
		while len(lines)>0 and not (lines[0] in ["INPUT","ENDTESTS"]):
			outs.append(lines.pop(0))
		outstr = "\n".join(outs)
		#hard_print("outstr: [[["+outstr+"]]]")
		tests.add(Test(ins,outstr))
	return tests

# add depth spaces before each line in this assumedly multi-line string s.
def indent(s, depth=6):
	depth_str = " "*depth
	return "\n".join(map(lambda line : (depth_str+line),s.split("\n")))

# put all their code in another file, also forcing it to be a function
# named student_main (indenting all they do).
def relocate_student_code(filename):
	# rename student's file, put it into a main function.
	prefix = "def student_main():\n"
	postfix = "\n"
	code = open(filename).read()
	f = open("student.py","w")
	f.write(prefix+indent(code)+postfix)
	f.close()

# not really needed anymore; just always wrote to stdout even during a program
# run that was recording outputs to a file with a repurposed print() target.
def hard_print(*args,**kwargs):
	print(*args, file=sys.__stdout__,**kwargs)

# relocate student's code; build all tests; run them; report answers.
def main():
	relocate_student_code(sys.argv[1])
	all_good = True
	count = 0
	tests = build_tests("tests.txt")
	(passed,total) = tests.run()
	print("\npassed %d/%d tests." % (passed,total))
	
	if os.path.exists("student.py"):
		os.remove("student.py")
	if os.path.exists("results.txt"):
		os.remove("results.txt")
	if os.path.exists("__pycache__"):
		shutil.rmtree("__pycache__")


# run it all.
if __name__ == "__main__":
	main()