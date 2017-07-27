import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story about a boy and his toys",
                        "https://lumiere-a.akamaihd.net/v1/images/open-uri20150422-20810-m8zzyx_5670999f.jpeg?region=0,0,300,450",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc"
                        )

#print(toy_story.storyline)

starwars = media.Movie("Star Wars: The Force Awakens",
                    "A new Hero rises to save the galaxy!",
                    "https://secure.netflix.com/us/boxshots/ghd/80058070.jpg",
                    "https://www.youtube.com/watch?v=sGbxmsDFVnE"
                    )

avatar = media.Movie("Avatar",
                    "A marine on an alien planet",
                    "https://images-na.ssl-images-amazon.com/images/M/MV5BMTYwOTEwNjAzMl5BMl5BanBnXkFtZTcwODc5MTUwMw@@._V1_UY1200_CR90,0,630,1200_AL_.jpg",
                    "https://www.youtube.com/watch?v=cRdxXPV9GNQ"
                    )

#print(avatar.storyline)
#avatar.show_trailer()

departed = media.Movie("The Departed",
                    "Mole vs Mole",
                    "https://images-na.ssl-images-amazon.com/images/M/MV5BMTI1MTY2OTIxNV5BMl5BanBnXkFtZTYwNjQ4NjY3._V1_UX182_CR0,0,182,268_AL_.jpg",
                    "https://www.youtube.com/watch?v=SGWvwjZ0eDc"
                    )

furious = media.Movie("The Fast and the Furious",
                    "Epic story about a street racing",
                    "http://vignette1.wikia.nocookie.net/fastandfurious/images/0/04/The_Fast_and_the_Furious_%28DVD_Cover%29.jpeg/revision/latest?cb=20150501043627",
                    "https://www.youtube.com/watch?v=ZsJz2TJAPjw"
                    )

idiocracy = media.Movie("Idiocracy",
                        "A soldier travels forwards in time to experience the future",
                        "https://www.thestoryoftexas.com/upload/images/events/movies/idiocracy-poster.jpg?1458770757",
                        "https://www.youtube.com/watch?v=BBvIweCIgwk"
                        )

transformers = media.Movie("Transformers",
                        "Robots in Disguise!",
                        "https://image.tmdb.org/t/p/w185_and_h278_bestv2/bgSHbGEA1OM6qDs3Qba4VlSZsNG.jpg",
                        "https://www.youtube.com/watch?v=yCOvcyfRPRk"
                        )

#print(idiocracy.storyline)
#idiocracy.show_trailer()

strangelove = media.Movie("Dr. Strangelove or: How I learned to stop worrying and love the bomb",
                        "An alternate ending to WWII",
                        "http://www.petertrumbore.com/wp-content/uploads/2016/03/strangelove.jpg",
                        "https://www.youtube.com/watch?v=1gXY3kuDvSU"
                        )

movies = [idiocracy, departed, furious, strangelove, transformers, starwars]
fresh_tomatoes.open_movies_page(movies)
#print(media.Movie.VALID_RAINGS)
#print(media.Movie.__name__)
#print(media.Movie.__module__)
