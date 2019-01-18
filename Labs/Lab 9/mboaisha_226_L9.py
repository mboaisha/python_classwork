def counts(sx):
    #Initilize empty dict and list
    temp_dict = {}
    temp_list = []
    
    #Find unique entries
    for x in sx:
        if x in temp_list:
            pass
        else:
            temp_list.append(x)
    
    #Update dict. with key and number of occurances
    for y in temp_list:
        if y not in temp_dict:
            counted = sx.count(y)
            temp_dict.update({y:counted})
    
       
    ans = temp_dict
    
    return ans

#XOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXO

def weeklies(plants_d):
    #Initlize empty list
    temp_list = []
    #Fetch key-value pairs one by one 
    for (k,v) in plants_d.items():
        if v == "weekly":
            #If the value of the dict == "Weekly" append to list
            temp_list.append(k)
    
    ans = temp_list
    #Return the ans.        
    return ans



#XOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXO

def closest(d, what, here):
    pass
#XOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXO
def file_counts(filename):
    pass

#XOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXO