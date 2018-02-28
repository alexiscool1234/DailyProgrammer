# [2018-02-06] Challenge #350 [Easy] Bookshelf problem
# https://www.reddit.com/r/dailyprogrammer/comments/7vm223/20180206_challenge_350_easy_bookshelf_problem/
# I am aware this isn't the optimised solution, but my maths is bad :(

totalShelf = 0
bookList = []
bookSizes = 0
shelfSpace = 0

shelveList = raw_input("Please enter the shelves: ").split(' ')
shelveList = [int(i) for i in shelveList]
shelveList = sorted(shelveList, reverse=True)
print "Sorted Shelves: %s" % shelveList


while True:
	book = raw_input("Please enter the books: ")
	if book != "":
		bookList.append(book)
	else:
		break
print "Books: %s" % (bookList)


for i in shelveList:
	totalShelf += i
print "Total shelf size: %s" % totalShelf


for i in bookList:
	bookLength = i.split(' ')
	bookSizes += int(bookLength[0])
print "Total book size: %s" % bookSizes

# if the total of books is more than item a, add it to a total and move onto b. Loop until successful.
# if end of list, print impossible.

for index, item in enumerate(shelveList):
	shelfSpace += item
	if bookSizes > shelfSpace:
		print "too big, continuing"
	elif bookSizes <= shelfSpace:
		print "Books filled by shelf number: %s" % index+1
		exit()
print "impossible"
