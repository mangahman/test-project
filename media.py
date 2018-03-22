import webbrowser
class Movie():
    def __init__(self , M_title,M_story,M_Poster,M_you):
        self.title = M_title
        self.story = M_story
        self.poster_image_url=M_Poster
        self.trailer_youtube_url=M_you
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)