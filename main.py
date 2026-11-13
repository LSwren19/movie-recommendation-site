from bakery import assert_equal
from dataclasses import dataclass
from drafter import *

set_website_title("Movie Recommendation")
set_site_information(
    author="Logan Wren",
    description="Easy way to find a movie to watch.",
    sources="Thanks to the Drafter docs and LLM",
    planning=[""],
    links=["https://github.com/LSwren19/movie-recommendation-site"]
)
hide_debug_information()
set_website_framed(False)

@dataclass
class Movie:
    title: str
    genre: str
    length: int
    era: str

@dataclass
class State:
    genre: str
    movie_length: int
    movie_era: str
    recommendations: list[Movie]
    
MOVIES = [
    # COMEDY

    # 1990s
    Movie("The Muppet Christmas Carol", "Comedy", 85, "1990s"),
    Movie("Clueless", "Comedy", 97, "1990s"),
    Movie("Mrs. Doubtfire", "Comedy", 128, "1990s"),

    # 2000s
    Movie("Borat", "Comedy", 84, "2000s"),
    Movie("Mean Girls", "Comedy", 97, "2000s"),
    Movie("Knocked Up", "Comedy", 133, "2000s"),
    
    # 2010s
    Movie("The Lego Movie", "Comedy", 100, "2010s"),
    Movie("Popstar: Never Stop Never Stopping", "Comedy", 87, "2010s"),
    Movie("The Wolf of Wall Street", "Comedy", 180, "2010s"),

    # 2020s
    Movie("Barbie", "Comedy", 114, "2020s"),
    Movie("Bad Trip", "Comedy", 84, "2020s"),
    Movie("Everything Everywhere All at Once", "Comedy", 139, "2020s"),

    # HORROR

    # 1990s
    Movie("Scream", "Horror", 111, "1990s"),
    Movie("The Ninth Gate", "Horror", 133, "1990s"),
    Movie("The Blair Witch Project", "Horror", 78, "1990s"),

    # 2000s
    Movie("The Mist", "Horror", 126, "2000s"),
    Movie("Saw", "Horror", 103, "2000s"),
    Movie("Paranormal Activity", "Horror", 86, "2000s"),
    # 2010s
    Movie("Get Out", "Horror", 104, "2010s"),
    Movie("Hush", "Horror", 87, "2010s"),
    Movie("It", "Horror", 135, "2010s"),

    # 2020s
    Movie("Nosferatu", "Horror", 133, "2020s"),
    Movie("Host", "Horror", 65, "2020s"),
    Movie("The Black Phone", "Horror", 103, "2020s"),

    # ACTION

    # 1990s
    Movie("Showdown in Little Tokyo", "Action", 79, "1990s"),
    Movie("The Matrix", "Action", 136, "1990s"),
    Movie("Speed", "Action", 116, "1990s"),

    # 2000s
    Movie("The Bourne Identity", "Action", 119, "2000s"),
    Movie("District 13", "Action", 81, "2000s"),
    Movie("The Dark Knight", "Action", 152, "2000s"),

    # 2010s
    Movie("John Wick", "Action", 101, "2010s"),
    Movie("Free Fire", "Action", 89, "2010s"),
    Movie("Avengers: Endgame", "Action", 181, "2010s"),

    # 2020s
    Movie("Nobody", "Action", 92, "2020s"),
    Movie("Top Gun: Maverick", "Action", 130, "2020s"),
    Movie("Zero", "Action", 82, "2020s"),

    # FANTASY

    # 1990s
    Movie("The Nightmare Before Christmas", "Fantasy", 76, "1990s"),
    Movie("Jumanji", "Fantasy", 104, "1990s"),
    Movie("The Green Mile", "Fantasy", 189, "1990s"),

    # 2000s
    Movie("The Chronicles of Narnia", "Fantasy", 143, "2000s"),
    Movie("Coraline", "Fantasy", 100, "2000s"),
    Movie("Cinderella III: A Twist in Time", "Fantasy", 74, "2000s"),

    # 2010s
    Movie("The BFG", "Fantasy", 117, "2010s"),
    Movie("The Shape of Water", "Fantasy", 123, "2010s"),
    Movie("Frankenweenie", "Fantasy", 87, "2010s"),

    # 2020s
    Movie("The Sea Beast", "Fantasy", 115, "2020s"),
    Movie("Shadow in the Cloud", "Fantasy", 83, "2020s"),
    Movie("The Green Knight", "Fantasy", 130, "2020s")
]

@route
def index(state: State) -> Page:
    '''
    '''
    return Page(state, [
        Header("Movie Generator"),
        Header("A tool to speed up the movie finding process", 2),
        Button("Select Genre", "select_genre")
    ])
        

@route
def select_genre(state: State, genre: str = '')-> Page:
    '''
    '''
    if genre:
        state.genre = genre
    return Page(state, [
        Header("Select a Genre"),
        "Current selection: " + state.genre,
        Button("Comedy", "select_genre",
               [Argument("genre", "Comedy")]),
        Button("Horror", "select_genre",
               [Argument("genre", "Horror")]),
        Button("Action", "select_genre",
               [Argument("genre", "Action")]),
        Button("Fantasy", "select_genre",
               [Argument("genre", "Fantasy")]),
        Button("Select Length", "select_length"),
    ])
    
@route
def select_length(state: State, length: int = 0) -> Page:
    '''
    '''
    if length:
        state.movie_length = length
    return Page(state, [
        Header("Select a Length"),
        "Current selection: " + str(state.movie_length),
        Button("Under 90 Minutes", "select_length",
               [Argument("length", 1)]),
        Button("90-120 Minutes", "select_length",
               [Argument("length", 2)]),
        Button("Over 120 Minutes", "select_length",
               [Argument("length", 3)]),
        Button ("Select Era", "select_era"),
    ])

@route
def select_era(state: State, era: str = '') -> Page:
    '''
    '''
    if era:
        state.movie_era = era
    return Page(state, [
        Header("Select an Era"),
        "Current selection: " + state.movie_era,
        Button("90s", "select_era",
               [Argument("era", "1990s")]),
        Button("00s", "select_era",
               [Argument("era", "2000s")]),
        Button("10s", "select_era",
               [Argument("era", "2010s")]),
        Button("20s", "select_era",
               [Argument("era", "2020s")]),
        Button ("Get Recommendations", "get_recommendations"),
    ])

@route
def get_recommendations(state: State) -> Page:
    state.recommendations  = []
    for movie in MOVIES:
        if movie.genre == state.genre and movie.era == state.movie_era:
            if state.movie_length == 1 and movie.length < 90:
                state.recommendations.append(movie)
            elif state.movie_length == 2 and movie.length >= 90 and movie.length <= 120:
                state.recommendations.append(movie)
            elif state.movie_length == 3 and movie.length > 120:
                state.recommendations.append(movie)
    return results(state)

@route
def results(state: State) -> Page:
    return Page(state, [
        Header("Your Movie Recommendation"),
        Table(state.recommendations),
        Button("Return Home", "return_home")
    ])

@route
def return_home(state: State) -> Page:
    state.genre = ""
    state.movie_length = 0
    state.movie_era = ""
    state.recommendations = []
    return index(state)
    
start_server(State("", 0, "", []))
