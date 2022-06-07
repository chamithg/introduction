x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]  
#1
x[1][0] = 15#-->1
students[0]["last_name"] = "Bryant" #--> 2
sports_directory["soccer"][0]= "Andreas"#--> 3
z[0]["y"]= 30 #-->4

#2
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def  iterateDictionary(some_list):
    for i in students:
        print("first_name -"+ i["first_name"])
        print("last_name- " + i["last_name"])

#3
def iterateDictionary2(key_name, some_list):
    for i in some_list:
        print(i[key_name])

#4
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printInfo(some_dict):
    for i in dojo:
        print(i)
        for j in dojo[i]:
            print(j)

printInfo(dojo)