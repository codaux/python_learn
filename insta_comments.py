
import instascrape

def getComments(url):
 postComments = Post(url)
 postComments.scrape()
 return postComments.get_recent_comments()

comments=getComments("https://www.instagram.com/p/CLnSbP7hOjh/")
for comment in comments:
   print(comment)