from instagrapi import Client
from instagrapi.types import StoryLink
from instagrapi.story import StoryBuilder
import imageio

imageio.plugins.ffmpeg.download()

cl = Client(proxy='http://123.123.123.123:40007')
cl.load_settings('/tmp/dump.json')

#cl = Client()
#cl.login("graphixilia", "aghareza712")

link = StoryLink(webUri="http://adw0rd.com")
buildout = StoryBuilder("G:/New/2.mp4", "Test").video(5, link=link.webUri)


cl.video_upload_to_story(buildout.path, "herererere", stickers=buildout.stickers)


#Story(pk='2737326000305270904', id='2737326000305270904_29817608135', code='CX8736KovB4', ....