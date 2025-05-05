#Set : It is a fundamental datastructure which is one of bulit in data types(Dictionary, List, Tuple, and set)
#Python provides built-in operations for performing set operation
#such as union, intersection, difference and symmetric difference
#set is created using curly bracket{}

mySet = {12,78,34,78}
print(mySet)

mySet2 = {76,34,22}
print(mySet2)
print(type(mySet))

#Uniou of two set using '|' operator
res=mySet | mySet2
print("The union of both the set", res)

#Using Union() method
res2=mySet.union(mySet2)
print("The union of both the set are", res2)

#INTERRSECTION OF TWO SETS
res = mySet & mySet2
print("The interasction of two sets",res)

#Set difference(-)
res=mySet-mySet2
print("The set difference of two sets",res)

#Symetric set difference(^)
res=mySet^mySet2
print("The symetric set difference of two sets",res)