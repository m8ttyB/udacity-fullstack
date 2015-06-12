#!/usr/bin/python
import fresh_tomatoes
from media import Movie

if __name__ == '__main__':
    # Create movie objects
    slither = Movie('Slither',
                    'http://www.halloweenonearth.com/halloween-movies/Slither.jpg',
                    'https://www.youtube.com/watch?v=2-f8wU6Fpeo')

    guardians = Movie('Guardians of the Galaxy',
                      'http://www.film-rezensionen.de/wp-content/uploads/2014/08/Guardians-of-the-Galaxy.jpg',
                      'https://www.youtube.com/watch?v=B16Bo47KS2g')

    wolf = Movie('The Wolf And The Medallion',
                 'http://blog.brandonhillphotos.com/wp-content/uploads/2011/07/wolf.teaser.square-1348x1024.jpg',
                 'https://www.youtube.com/watch?v=dlTJ8MTCPjA')

    priscilla = Movie('Priscilla Queen Of The Desert',
                      'http://media-cache-ec0.pinimg.com/736x/2d/bd/2e/2dbd2e1f3119614664828121a486e0e8.jpg',
                      'https://www.youtube.com/watch?v=QgFDIinCeYI')

    # Create a list of movies
    movies = [slither, guardians, wolf, priscilla]

    # Generate HTML file using the movies list
    fresh_tomatoes.open_movies_page(movies)
