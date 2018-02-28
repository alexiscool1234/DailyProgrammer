a, b ,c = raw_input("Enter your name, age and username seperated by spaces: ").split(" ")

str = "your name is %s, you are %s years old, and your username is %s" % (a,b,c)

with open ("output.txt", "w") as text_file:
	text_file.write(str)
	print str
	text_file.close()
