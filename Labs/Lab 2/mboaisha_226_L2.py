#mboaisha_226_L2

#-------------------------------------------------------------------------------
# Name: Mohammad H. BoaISHA.
# G#: G00901310.
# Lab 2
# Lab Section 226
#-------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that
# violates the ethical guidelines set forth by professor and class syllabus.
#-------------------------------------------------------------------------------
# References: list any lecture slides, text book pages, any other (allowed)
# resources you've used.
#-------------------------------------------------------------------------------
# Comments and assumptions: A note to the grader as to any problems or
# uncompleted aspects of the assignment, as well as any assumptions about the
# meaning of the specification.
#-------------------------------------------------------------------------------
# NOTE: width of source code should be <= 80 characters to facilitate printing.
#2345678901234567890123456789012345678901234567890123456789012345678901234567890
# 10 20 30 40 50 60 70 80
#-------------------------------------------------------------------------------

#score = int(input("What's your score?: "))

'''
Grading
A+ -> 98
A -> 92
A- -> 90
B+ -> 88
B -> 82
B- -> 80
C+ -> 78
C -> 72
C- -> 70
D -> 60
F -> 59-

'''

#Letter grade function
def letter_grade(score):
	if score >= 98:
		assignScore = 'A+'

	elif score >= 92:
		assignScore = 'A'

	elif score >= 90:
		assignScore = 'A-'

	elif score >= 88:
		assignScore = 'B+'

	elif score >= 82:
		assignScore  = 'B'

	elif score >= 80:
		assignScore = 'B-'

	elif score >= 78:
		assignScore = 'C+'

	elif score >= 72:
		assignScore = 'C'

	elif score >= 70:
		assignScore = 'C-'

	elif score >= 60:
		assignScore = 'D'

	else:
		assignScore = 'F'

	return assignScore


a = input("value a: ")
b = input("value b: ")
c = input("value c: ")

def sum2biggest(a,b,c):
	sum = 0

	if (a > b) and (a > c):
		
		if b > c:
			sum = int(a) + int(b)

		elif c > b:
			sum = int(a) + int(c)

	elif (a==b) or (a==c):
		if a == b:
			sum = int(a) + int(b)

		if c == b:
			sum = int(a) + int(b)

		if a == c:
			sum = int(a) + int(c) 
	
	return print(sum)


sum2biggest(a,b,c)



