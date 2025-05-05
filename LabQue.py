'''
You manage course registration in a university. you have two set:

set A : students enrolled in data science
set B : student enrolled in web development

consider data set like
data_science_student = {"Alice", "Bob", "Charile", "David"}
web_dev_student = {"Charlie", "Eve", "Frank", "BOb"}
'''
#WAP to solve following queries:
data_science_student = {"Alice", "Bob", "Charile", "David"}
web_dev_student = {"Charlie", "Eve", "Frank", "Bob"}

#1.Student enrolled in at least one course
atleast_one_course = data_science_student.union(web_dev_student)
print("Students enrolled in at least one course:", atleast_one_course)

#2.Student enrolled in both courses
both_courses = data_science_student.intersection(web_dev_student)
print("Students enrolled in both courses:", both_courses)

#3.Student enrolled in data Science but not in Web Development
data_science_but_not_web_dev = data_science_student.difference(web_dev_student)
print("Students enrolled in data science but not in web development:", data_science_but_not_web_dev)

#4.Student enrolled in exactly one cource
exactly_one_course = data_science_student.symmetric_difference(web_dev_student)
print("Students enrolled in exactly one course:", exactly_one_course)