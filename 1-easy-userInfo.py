name = raw_input("Name?: ")
age = raw_input("Age?: ")
username = raw_input("Username?: ")

print "your name is %s, you are %s years old, and your username is %s" % (name,age,username)
with open ("output.txt", "w") as text_file:
	text_file.write("your name is %s, you are %s years old, and your username is %s" % (name,age,username))