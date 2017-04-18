import feedparser
import datetime
import dateutil.parser
def RssToList(request):
	feed = feedparser.parse(request)["entries"]
	TitleFeeds =[]
	LinkFeeds = []
	PublishedFeeds = []
	for i in feed:
		TitleFeeds.append(i["title"])
		LinkFeeds.append(i["links"][0]["href"])
		PublishedFeeds.append("-".join(i["published"].split(",")[1].split()[0:-1]))
	return zip(TitleFeeds,LinkFeeds,PublishedFeeds)

List = RssToList("http://showrss.info/user/132011.rss?magnets=true&namespaces=true&name=null&quality=null&re=null")

for i in List:
	print i
print List.sort(key=lambda x: datetime.datetime.strptime(dateutil.parser.parse(x[2])), '%Y-%m%d %H-%M-%S')

