# Exercise: Using your first API

# API documentation: http://bechdeltest.com/api/v1/doc

# Goal 1:
#   Ask the user for the movie title they want to check
#   Display all of the details about the movie returned by the API
#
#   Things to keep in mind:
#       How will your program behave when multiple movies are returned?
#       How will your program behave when no movies are returned?
#       How will your program behave with works like "the" in the title?

import requests
import json

requested_movie = raw_input("What movie do you want to check? ")

link_to_get = "http://bechdeltest.com/api/v1/getMoviesByTitle?title={0}".format(requested_movie).replace(" ", "+")

#print link_to_get

response = requests.get(link_to_get).json()
#print response

#fixing "the" problem
requested_movie = requested_movie.strip('The')

print "Movie and and score:"

for movie in response: 
    print movie['title'], movie['rating']

# Goal 2:
#   Check to see if the user input is a movie title or an ImdbID and use the proper endpoint

#Wanted to add in a response if there movie can't be found
if response == []:
    print "No movie found, try again"

#is it an idmbID 
is_imdb = requested_movie.isdigit()

if is_imdb == True:
   print "Looks like you are using a IMDBid, use a movie name"

# Goal 3:
# Integrate this with the Open Movie Database API: http://www.omdbapi.com/
#   Display all of the details from both APIs when searching for a movie.
#   Note that you may need to prefix your ImdbIDs with 'tt' to get the search to work.

link_to_get_imdb = "http://www.omdbapi.com/?t={0}".format(requested_movie).replace(" ", "%20")

print link_to_get_imdb

imdb_response = requests.get(link_to_get_imdb).json()

print imdb_response

print "Movie info from IMDB:"

for thing in imdb_response:
   print thing['Rated']


# Copy these URLs into your browser!
# To visualize as a CSV, copy the JSON into http://konklone.io/json

# Sample Bechdel test API returns: http://bechdeltest.com/api/v1/getMovieByImdbId?imdbid=0367631
# JSON: 
    # {
    #   "visible": "1",
    #   "date": "2009-12-05 05:13:37",
    #   "submitterid": "270",
    #   "rating": "3",
    #   "dubious": "0",
    #   "imdbid": "0367631",
    #   "id": "551",
    #   "title": "D.E.B.S.",
    #   "year": "2004"
    # }
# JSON to CSV link: http://konklone.io/json/?id=11488879

# Sample Open Movie Database API returns: http://www.omdbapi.com/?i=tt0367631&t=
# JSON:
    # {
    #   "Title": "D.E.B.S.",
    #   "Year": "2004",
    #   "Rated": "PG-13",
    #   "Released": "25 Mar 2005",
    #   "Runtime": "91 min",
    #   "Genre": "Action, Comedy, Romance",
    #   "Director": "Angela Robinson",
    #   "Writer": "Angela Robinson",
    #   "Actors": "Sara Foster, Jordana Brewster, Meagan Good, Devon Aoki",
    #   "Plot": "Plaid-skirted schoolgirls are groomed by a secret government agency to become the newest members of the elite national-defense group, D.E.B.S.",
    #   "Language": "English",
    #   "Country": "USA",
    #   "Awards": "1 win & 2 nominations.",
    #   "Poster": "http://ia.media-imdb.com/images/M/MV5BMjA0OTU5ODgyOF5BMl5BanBnXkFtZTcwODczNDgyMQ@@._V1_SX300.jpg",
    #   "Metascore": "42",
    #   "imdbRating": "5.2",
    #   "imdbVotes": "10,563",
    #   "imdbID": "tt0367631",
    #   "Type": "movie",
    #   "Response": "True"
    # }
# JSON to CSV link: http://konklone.io/json/?id=11488839
