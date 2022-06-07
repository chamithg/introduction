def countdown(number):
    list =[]
    for i in range(number,-1,-1):
        list.append(i)
    return list

print(countdown(5))

def print_and_return(list):
    print(list[0])
    return list[1]

print(print_and_return([1,2]))


def first_plus_length(list):
    return list[0]+len(list)

print(first_plus_length([1,2,3,4,5]))


def value_greater_than_second(list):
    new_list =[]
    if len(list) > 2: 
        for i in range(0,len(list)):
            if list[i]> list[1]:
                new_list.append(list[i])
        return new_list
    else:
        return False   

print(value_greater_than_second([3]))

def this_length_that_value(par_1,par_2):
    list =[]
    for i in range(0, par_1):
        list.append(par_2)
    return list

print(this_length_that_value(6,7))