import media
import fresh_tomatoes

# Star Wars with movie info
starwars = media.Movie(
    "Star Wars: The Force Awakens",
    "A new Hero rises to save the galaxy!",
    "https://secure.netflix.com/us/boxshots/ghd/80058070.jpg",  # NOQA
    "https://www.youtube.com/watch?v=sGbxmsDFVnE"
    )

# The Departed with movie info
departed = media.Movie(
    "The Departed",
    "Mole vs Mole",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BMTI1MTY2OTIxNV5BMl5BanBnXkFtZTYwNjQ4NjY3._V1_UX182_CR0,0,182,268_AL_.jpg",  # NOQA
    "https://www.youtube.com/watch?v=SGWvwjZ0eDc"
    )

# The Fast and the Furious with movie info
furious = media.Movie(
    "The Fast and the Furious",
    "Epic story about a street racing",
    "http://vignette1.wikia.nocookie.net/fastandfurious/images/0/04/The_Fast_and_the_Furious_%28DVD_Cover%29.jpeg/revision/latest?cb=20150501043627",  # NOQA
    "https://www.youtube.com/watch?v=ZsJz2TJAPjw"
    )

# Idiocracy with movie info
idiocracy = media.Movie(
    "Idiocracy",
    "A soldier travels forwards in time to experience the future",
    "https://www.thestoryoftexas.com/upload/images/events/movies/idiocracy-poster.jpg?1458770757",  # NOQA
    "https://www.youtube.com/watch?v=BBvIweCIgwk"
    )

# Transformers with movie info
transformers = media.Movie(
    "Transformers",
    "Robots in Disguise!",
    "https://image.tmdb.org/t/p/w185_and_h278_bestv2/bgSHbGEA1OM6qDs3Qba4VlSZsNG.jpg",  # NOQA
    "https://www.youtube.com/watch?v=yCOvcyfRPRk"
    )

# Dr Strangelove with movie info
strangelove = media.Movie(
    "Dr. Strangelove or: How I learned to stop worrying and love the bomb",
    "An alternate ending to WWII",
    "http://www.petertrumbore.com/wp-content/uploads/2016/03/strangelove.jpg",  # NOQA
    "https://www.youtube.com/watch?v=1gXY3kuDvSU"
    )

# Set movies array that will be passed into media.py
movies = [idiocracy, departed, furious, strangelove, transformers, starwars]

# Open the HTML file in a webbrowser
fresh_tomatoes.open_movies_page(movies)
