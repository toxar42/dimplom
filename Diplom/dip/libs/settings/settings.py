import pathlib
class Colors():
    def __init__(self):
        self.darkgrey = '#343a40'
        self.lightgrey = '#adb5bd'
        self.lighttext = '#e9ecef'
        self.darktext = '#212529'
    

class Pathes():
    def __init__(self):
        self.path_app = str(pathlib.PurePath(__file__).parent.parent)

        self.bg = self.path_app + '/images/'
        self.logo = self.path_app + '/icons/'
        self.no_user_image = self.path_app + '/images/user.png'