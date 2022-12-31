from InstagramAPI import InstagramAPI

 
user = "graphixilia"
password = "aghareza712"
InstagramAPI = InstagramAPI(user, password)
InstagramAPI.login()
photo_path = 'G:/New/1.jpg'
InstagramAPI.uploadPhoto(photo_path)