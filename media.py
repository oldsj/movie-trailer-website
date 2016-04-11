import webbrowser


class Video:
    valid_ratings = ["G", "PG", "PG-13", "R"]

    def __init__(self, title, summary, rating, poster_image, trailer):
        self.title = title
        self.summary = summary
        if rating in self.valid_ratings:
            self.rating = rating
        else:
            raise IndexError('Please give a valid rating')
        self.poster_image = poster_image
        self.trailer = trailer

    def show_trailer(self):
        webbrowser.open(self.trailer)


class Movie(Video):

    def __init__(self, title, summary, rating, poster_image, trailer):
        Video.__init__(self, title, summary, rating, poster_image, trailer)
