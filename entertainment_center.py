import media
import fresh_tomatoes

primer = media.Movie("Primer",
                     "While conducting experiments in a garage, " +
                     "two brilliant engineers who lead double lives " +
                     "accidentally discover that their project enables " +
                     "them to travel back in time.",
                     "PG-13",
                     "https://upload.wikimedia.org/wikipedia/en/f/f7/Primer_" +
                     "%282004_film_poster%29.jpg",
                     "https://www.youtube.com/watch?v=9A7fCKM4ERA")
no_country = media.Movie("No Country for Old Men",
                         "A dumb movie that makes no sense",
                         "R",
                         "https://upload.wikimedia.org/wikipedia/en/8/8b/No_" +
                         "Country_for_Old_Men_poster.jpg",
                         "https://www.youtube.com/watch?v=YBqmKSAHc6w")
interstellar = media.Movie("Interstellar",
                           "An awesome movie about black holes",
                           "R",
                           "https://upload.wikimedia.org/wikipedia/en/b/bc/" +
                           "Interstellar_film_poster.jpg",
                           "https://www.youtube.com/watch?v=zSWdZVtXT7E")

movies = [primer, no_country, interstellar]
fresh_tomatoes.open_movies_page(movies)
#test commit
