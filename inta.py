from instagrapi import Client
from instagrapi.types import Hashtag, StoryHashtag, StoryLink

cl = Client()
#cl = Client(proxy='http://123.123.123.123:40007')

cl.login("graphixilia", "aghareza712")
#sHashtag = "dfgergewr"
#cl.video_upload_to_story("G:/New/2.mp4", "hereeeeeeeeeeee", links=[StoryLink(webUri="http://adw0rd.com")] ,
#hashtags=[StoryHashtag(Hashtag=sHashtag, x=0.23, y=0.32, width=0.5, height=0.22)],

cl.photo_upload_to_story('G:/New/1.jpg', "", links=[StoryLink(webUri="http://adw0rd.com")])
