# LAB EXERCISE 04

# SET UP BEGINS - Do Not Modify
movie_data = [
    ["Inception", 2010, 8.8, "Sci-Fi", 829.9], 
    ["The Shawshank Redemption", 1994, 9.3, "Drama", 28.3], 
    ["The Godfather", 1972, 9.2, "Crime", 134.8], 
    ["The Dark Knight", 2008, 9.0, "Action", 1005.0], 
    ["The Matrix", 1999, 8.7, "Sci-Fi", 467.2], 
    ["Interstellar", 2014, 8.6, "Sci-Fi", 701.8], 
    ["Forrest Gump", 1994, 8.8, "Drama", 678.2], 
    ["The Lord of the Rings: The Return of the King", 2003, 8.9, "Fantasy", 1142.5], 
    ["Pulp Fiction", 1994, 8.9, "Crime", 213.9], 
    ["The Lion King", 1994, 8.5, "Animation", 968.5],
    ["Fight Club", 1999, 8.8, "Drama", 101.2],
    ["Gladiator", 2000, 8.5, "Action", 460.5],
    ["Titanic", 1997, 7.9, "Romance", 2187.5],
    ["Jurassic Park", 1993, 8.2, "Adventure", 1045.7],
    ["The Avengers", 2012, 8.0, "Action", 1518.8],
    ["Avatar", 2009, 7.8, "Sci-Fi", 2923.7],
    ["The Silence of the Lambs", 1991, 8.6, "Thriller", 272.7],
    ["Saving Private Ryan", 1998, 8.6, "War", 482.3],
    ["The Departed", 2006, 8.5, "Crime", 291.5],
    ["Whiplash", 2014, 8.5, "Drama", 49.0]
]
# SET UP ENDS - Do Not Modify


# PROBLEM 01
class Movie:
    """
    Represents a movie with basic metadata and performance information.
    
    Attributes:
        title (str): The title of the movie.
        year (int): The year the movie was released.
        rating (float): The movie's rating (0.0 to 10.0).
        genre (str): The genre of the movie.
        box_office (float): Box office revenue in millions of dollars.

    Methods:
        __init__(): Initializes all movie attributes.
        is_highly_rated(): Returns True if the movie's rating is 8.0 or above,
            False otherwise.
    """
    pass #TODO implement

# PROBLEM 02
def create_movie_objects(movie_data):
    """this function takes a list of lists and returns a list of movie objects"""
    movies= []

    for movie in movie_data:

        movies.append(Movie(*movie))

    return movies

# PROBLEM 03


# PROBLEM 04

def analyze_genre(movies, genre):
    """
    Summarizes the movies in a given genre.

    Args:
        movies (list): A list of Movie objects.
        genre (str): The genre to analyze.

    Returns:
        dict: A dictionary with the keys "count" (number of movies in the
            genre), "avg_rating" (average rating, rounded to 2 decimal
            places), "total_box_office" (total box office revenue, rounded
            to 2 decimal places), and "highly_rated_count" (number of
            highly rated movies in the genre). All values are 0 if no
            movies match the genre.
    """
    genre_movies = [movie for movie in movies if movie.genre == genre]

    if not genre_movies:
        return {"count": 0, "avg_rating": 0, "total_box_office": 0,
                "highly_rated_count": 0}

    count = len(genre_movies)
    total_rating = sum(movie.rating for movie in genre_movies)
    total_box_office = sum(movie.box_office for movie in genre_movies)
    highly_rated_count = sum(1 for movie in genre_movies
                             if movie.is_highly_rated())

    return {"count": count,
            "avg_rating": round(total_rating / count, 2),
            "total_box_office": round(total_box_office, 2),
            "highly_rated_count": highly_rated_count}


def main():
    pass

if __name__ == '__main__':
    main()

