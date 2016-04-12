import webbrowser


class Video:
    """ This is the super class for all video media types.
    Attributes:
        title (str): The title of the video
        summary (str): A quic summary of the video
        rating (str): A rating of the video's content
        poster_image (str): a poster picture of the video
        trailer (str): a link to the trailer for the video on youtube
    """
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
        """ opens the default webbrowser with the given trailer link"""
        webbrowser.open(self.trailer)


class Movie(Video):
    """ Subclass of Video. Right now it is 1:1 with Video, but having it split
    out like this will allow the addition of other types of video (ex tv shows)
    in the future.

    Attributes:
        Same as Video
    """

    def __init__(self, title, summary, rating, poster_image, trailer):
        Video.__init__(self, title, summary, rating, poster_image, trailer)


class TvShow(Video):
    """ Not in use yet, but allows for TV shows to be added as well
    Attributes:
        episode (int): specifies the tv show's episode number
    """
    def __init__(self, title, summary, rating, poster_image, trailer, episode):
        Video.__init__(self, title, summary, rating, poster_image, trailer)
        self.episode = episode
