import media
import fresh_tomatoes


# This module constructs instances of movies from the media.py classes.
primer = media.Movie("Primer",
                     "While conducting experiments in a garage, " +
                     "two brilliant engineers who lead double lives " +
                     "accidentally discover that their project enables " +
                     "them to travel back in time.",
                     "PG-13",
                     # NOQA
                     "https://upload.wikimedia.org/wikipedia/en/f/f7/Primer_%282004_film_poster%29.jpg",
                     "https://www.youtube.com/watch?v=9A7fCKM4ERA")
no_country = media.Movie("No Country for Old Men",
                         "Violence and mayhem ensue after a hunter stumbles" +
                         "upon a drug deal gone wrong and more than two" +
                         "million dollars in cash near the Rio Grande.",
                         "R",
                         # NOQA
                         "https://upload.wikimedia.org/wikipedia/en/8/8b/No_Country_for_Old_Men_poster.jpg",
                         "https://www.youtube.com/watch?v=YBqmKSAHc6w")
interstellar = media.Movie("Interstellar",
                           "A team of explorers travel through a wormhole in" +
                           "space attempting to ensure humanity's survival.",
                           "R",
                           # NOQA
                           "https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg",
                           "https://www.youtube.com/watch?v=zSWdZVtXT7E")

# store instances of movies
movies = [primer, no_country, interstellar]
# pass the movie instances to fresh_tomatoes to build the html file
fresh_tomatoes.open_movies_page(movies)
