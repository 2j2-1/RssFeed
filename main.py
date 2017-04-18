import feedparser
import datetime
import dateutil.parser

FEEDS = []
file = open("Feeds.txt","r")
for line in file:
	FEEDS.append(line)
file.close()

def URLsToFeed():
	allFeeds =[]
	for request in FEEDS:
		feed = feedparser.parse(request)["entries"]
		currentFeed =[]
		for Elements in feed:
			currentFeed.append([Elements["title"],
						Elements["links"][0]["href"]])
						# ,dateutil.parser.parse("-".join(Elements["published"].split(",")[1].split()[0:-1]))
		allFeeds.append(currentFeed)
	return allFeeds

def ConcatAllFeed(feed):
	List = []
	for i in feed:
		List += i
	return List

def PrintFeed(feed):
	try:
		file = open("ReadFeeds.txt","r")
		read = []
		for i in file:
			read.append(i)
		read = ("".join(read)).split("\n")
		file.close()
	except:
		read=[]
	try:
		for i in sorted(feed,key=lambda x: x[2], reverse=True):
			if i[0] not in read:
				try:
					ReadElements(i[0])
					for j in i:
						print j
				except:
					pass
				
				print 
	except:
		for i in feed:
			if i[0] not in read:
				try:
					ReadElements(i[0])
					for j in i:
						print j
				except:
					pass
				
				print 

	

def ReadElements(Elements):
	file = open("ReadFeeds.txt","a")
	file.write(Elements+"\n")
	file.close()
def Menu():
	ALLFEEDS = URLsToFeed()
	print "Rss Reader - 2j2-1"
	print "1. Read All Feeds"
	print "2. Read Indivdual Feeds"
	print "3. Settings \n"
	choice = input("Input Choice: ")
	print 
	if choice == 1:
		PrintFeed(ConcatAllFeed(ALLFEEDS))
	elif choice == 2:
		print "\nView:"
		for i in range(len(FEEDS)):
			print str(i+1) + " " + feedparser.parse(FEEDS[i])["feed"]["title"]
		print
		PrintFeed(ALLFEEDS[input("Input Choice: ")-1])
	elif choice == 3:
		print "1. Add Feeds\n2. Delete Feeds\n"
		SettingChoice = input("Input Choice")
		if SettingChoice == 1:
			file = open("Feeds.txt","a")
			file.write(raw_input("Input Feed URL"))
		elif SettingChoice == 2:
			file = open("Feeds.txt","r+")
			print file.read()
			EditFeeds = []
			for i in file.read():
				print i



Menu()



