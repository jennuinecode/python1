# part 1
# students = [
#      {'first_name':  'Michael', 'last_name' : 'Jordan'},
#      {'first_name' : 'John', 'last_name' : 'Rosales'},
#      {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#      {'first_name' : 'KB', 'last_name' : 'Tonel'}
# ]
#
# for i in students:
#     print i['first_name'] , i['last_name']

# part 2

users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
     ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
     ]
 }

print "Students:"

student_row = 1
for i in users['Students']:
    full_name = len(i['first_name'] + i['last_name'] )
    print student_row , i['first_name'].upper() , i['last_name'].upper() , '-', full_name
    student_row = student_row + 1

print "Instructors:"

instructor_row = 1
for i in users['Instructors']:
    full_name = len(i['first_name'] + i['last_name'] )
    print instructor_row, i['first_name'].upper() , i['last_name'].upper() , '-', full_name
    instructor_row = instructor_row + 1
