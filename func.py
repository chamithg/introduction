def sample_function_name (par_a, par_b):
    #create a new list
    #add numbers to that list in the range par a to b 
    list =[]
    for x in range(par_a,par_b+1):
        list.append(x)
        
    return list


list1 = sample_function_name(4,7)
print(list1)