#mboaisha_226_P2

#-------------------------------------------------------------------------------
# Name: Mohammad H. BoaISHA.
# G#: G00901310.
# Project 2
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


weight_package = float(input("Weight of shipment(lbs): "))


if weight_package < float(50.00): #Check for weight

	expCheck = input("Express shipment?") #Check for express option 
	if expCheck == "y" or expCheck == "yes" or expCheck == "Yes":

		distance = input("Distance of shipment(miles): ") #Get distance
		
		if float(distance) > 12450.00: #Check if if the distance is legal
			print("Out of range of Earth's surface!")
			
	elif expCheck == "n" or expCheck == "no" or expCheck == "No":
		float(weight_package)
		nonExpPrice = weight_package * 0.50
		print("\nThat will cost you: " + str(nonExpPrice) + "$")



else:
	print("Too heavy!")

