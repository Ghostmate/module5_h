class DBVideo:
    def __init__(self):
        self.data = {}

    def add_video(self, title, video):
        self.data[title] = video

    def __getitem__(self, item):
        return self.data[item]
