dict={
    "name":"Agin K.K",
    "age":21,
    "place":"calicut"
}
print(dict)

#--------change value ------

dict["age"]=20
print(dict)

#--------Operations in dictionary---------

print(dict["name"])

print(dict.get("age"))

dict.update({
    "name":"Certification Course",
    "course":"MCA"
})
print(dict)

del dict["course"]
print(dict)
