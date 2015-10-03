import sys

sys.path.append("C:\Users\M\Documents\Web Development\Udacity\Full Stack Developer\movies\Media.py")

import fresh_tomatoes
import Media

toy_story = Media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")
print(toy_story.movie_title)


##avatar = Media.Movie("Avatar",
##                     "A marine on an alien planet",
##                     "http://slavomirkrestian.com/wp-content/uploads/2015/01/free-movie-film-poster-avatar_xlg.jpg",
##                     "www.youtube.com/watch?v=d1_JBMrrYw8")
##
###print(avatar.storyline)
###avatar.show_trailer()
##
##fist_of_legend = Media.Movie("Fist of Legend", "Quickest Fist of the East", "http://www.framedart.com/product-images/AWAAQAHQ-P182107.jpg",
##                        "https://www.youtube.com/watch?v=LPEzoOifD1k")
##
##enter_the_dragon = Media.Movie("Enter The Dragon", "Numchuck Professional", "http://www.framedart.com/product-images/AWAAQAHQ-P185892.jpg",
##                        "https://www.youtube.com/results?search_query=enter+the+dragon+trailer")
##
##taken_2 = Media.Movie("Taken 2", "A Father's Love", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRsDnxprU3rV9R4jEGMJ_Ihqw1IS14ur0qVHLpMjLvo2NfKLUsdBQ",
##                        "https://www.youtube.com/watch?v=u48UrWtCn5E")
##
##the_dark_knight = Media.Movie("The Dark Knight", "Batman's Revenge", "http://www.freedesign4.me/wp-content/gallery/posters/free-movie-film-poster-the_dark_knight_movie_poster.jpg",
##                        "https://www.youtube.com/watch?v=4S9a5V9ODuY")
##
##movies = [toy_story, avatar, fist_of_legend, enter_the_dragon, taken_2, the_dark_knight]
###fresh_tomatoes.open_movies_page(movies)
###print(Media.Movie.VALID_RATINGS)
##print(Media.Movie.__doc__)

