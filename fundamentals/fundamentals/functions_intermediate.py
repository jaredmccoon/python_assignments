# 1
# x = [ [5,2,3], [10,8,9] ] 
# students = [
#     {'first_name':  'Michael', 'last_name' : 'Jordan'},
#     {'first_name' : 'John', 'last_name' : 'Rosales'}
# ]
# sports_directory = {
#     'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
#     'soccer' : ['Messi', 'Ronaldo', 'Rooney']
# }
# z = [ {'x': 10, 'y': 20} ]

# def change():
#     x[1][0] = 15
#     students[0]['last_name'] = 'bryant'
#     sports_directory['soccer'][0] = 'Andres'
#     z[0]['y'] = 30
#     print(x[1][0])
#     print(students)
#     print(sports_directory)
#     print(z)

# print(change())


# # 2
# students = [
#         {'first_name':  'Michael', 'last_name' : 'Jordan'},
#         {'first_name' : 'John', 'last_name' : 'Rosales'},
#         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#         {'first_name' : 'KB', 'last_name' : 'Tonel'}
#     ]
# def iterateDictionary():
#     for i in range(len(students)):
#         for key, value in students[i].items():
#             print(key, '-', value)

# print(iterateDictionary())

# 3
# def iterateDictionary2(some_key, some_list):
#     for i in range(len(students)):
#         print(some_list[i][some_key])
            

# print(iterateDictionary2('first_name', students))
# print(iterateDictionary2('last_name', students))

# 4

# dojo = {
#     'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
#     'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
# }
# def printInfo():
#     for key, value in dojo.items():
#         print(len(dojo[key]), key)
#         def items(write):
#             for i in range(len(write)):
#                 print(write[i])
#         print(items(dojo[key]))
    

# print(printInfo())