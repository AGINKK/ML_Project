list =[10,20,30,40,50]
print(list)

fruits=["Apple","Orange","Banana"]
print(fruits)

#--------------PYTHON OPERATIONS -----------------------------------------

#---append()---------
fruits.append("cherry")
print(fruits)

#----insert()--------
fruits.insert(1,"Avacado")
print(fruits)

#---------extend()-----
fruits.extend(["grape","blueberry","pineapple"])
print(fruits)

#------count()---------
fruits.count("cherry")
print(fruits.count("cherry"))

#-----sort()-----------
fruits.sort()
print(fruits)

#---------reverse()--------
fruits.reverse()
print(fruits)

#-------remove------
fruits.remove("pineapple")
print(fruits)
