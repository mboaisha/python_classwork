def rank3(x,y,z, ascending=True):
    if ascending == False:
        temp_tuple = (x,y,z)
        return temp_tuple
    elif ascending == True:
        temp_list = [x,y,z]
        #Sort routine
        temp_list.sort()
        
        return tuple(temp_list)

def remove(val,xs,limit=None):
	if limit == None:
	    while val in xs:
	        xs.remove(val)
	 
	else:
	    counter = limit
	    while True:
	        if val in xs and counter > 0:
	            xs.remove(val)
	            counter -= 1
	        else:
	            return xs
	    
	
	return xs



