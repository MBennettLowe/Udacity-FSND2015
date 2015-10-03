import webbrowser
class Movie():
    """In this project you will build a Movie Trailer Website where users can see
        your favorite movies and watch the trailers.""" 
    
 
    def __init__(self, movie_title, movie_storyline, movie_actors, movie_release_date, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.actors = "Stars: " + movie_actors
        self.release_date = "Release date: " + movie_release_date
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
        
   


       





    
        

    
