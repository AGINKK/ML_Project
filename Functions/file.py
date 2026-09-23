file=open("student.txt","w")
file.write("Hello,World!\n")
file.write("This is a new line./n")

# lines = [
#     "Name: Alice\n",
#     "Age: 20\n",
#     "Grade: A\n"
# ]

# file = open("student.txt", "w")
# file.writelines(lines)
# file.close()

# name = "John"
# score = 95

# file = open("student.txt", "w")
# file.write(f"Student: {name}\n")
# file.write(f"Score: {score}\n")
# file.close()

file = open("student.txt", "r")
content = file.read(5)
single_line = file.readline()
all_lines = file.readlines()
file.close()