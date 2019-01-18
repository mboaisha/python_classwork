#
# Name: Mohammad H. BoAisha 
# G#: G00901310
# Lecture sec.:
# Lab sec.: 
#
def odd_product(xs):
	#Filter out odd numbers and append to a list
    temp_list = []
    product = 1
    for x in xs:
        if x % 2 == 0:
            pass
        else:
            temp_list.append(x)

    for x in temp_list:
        #Multiply each iteration to the product
        product *= x
    #Explicitely convert the format to int
    ans = int(product)
    return ans

def divisor(n):
	pass

def has_duplicates(xs):
    ans = None
    #Initilize type of xs
    xs_type = str(type(xs))
    #... and an empty list
    temp_list = []
    #..... and an empty string
    temp_str = ""
    #First run, works for list of integars
    for x in xs:
        if x in xs and x not in temp_list:
            temp_list.append(x)
        elif x in xs and x in temp_list:
            ans = True
            break;
        if temp_list == xs:
            ans = False
            
            #Join string
            #Check if xs is a string
    if xs_type == "<class 'str'>":
        for x in xs:
            temp_str += x
            
    #After joining string, simply compare in a second run
    xs_len = len(xs)
    temp_list_len = len(temp_list)
    temp_str_len = len(temp_str)
    for x in temp_list:
        if len(xs) == len(temp_list):
            ans = "False"
        elif len(xs) != len(temp_list):
            ans = "True"
            break;
     
    return ans

	
def truncatable_prime(n):
	pass

def histogram(xs):
	pass

def second_smallest(xs):
	pass
	#temp1_list = xs

	
	

def mode(xs):
	pass

