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
    '''
    Represents a movie in a collection of movies
    title: name of the movie, genre: genre of the movie, length: movie runtime in minutes, era: decade the movie was released.
    '''
    title: str
    genre: str
    length: int
    era: str

@dataclass
class State:
    '''
    Stores the users selections and movie recommendation
    genre: genre selected by user, movie_length: selected movie runtime, movie_era: selected release date decade, recommendations: list of movies matching the users selections
    '''
    genre: str
    movie_length: int
    movie_era: str
    recommendations: list[Movie]
    
MOVIES = [

# A dataset of movies is provided as possible recommendations. There is a movie that fits every possible combination the user could enter, leaving no black recommendations or errors.

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
    This is how the Movie Generator Home Page is displayed
    Args - An introduction is provided as well as a path to follow along with
    Returns - state: the current website, Page containing the home page content
    '''
    return Page(state, [
        Header("Movie Generator"),
        Header("A tool to speed up the movie finding process", 2),
        Button("Select Genre", "select_genre")
    ])

assert_equal(index(State("Comedy", 1, "2020s", [])).state.genre, "Comedy")
assert_equal(index(State("Horror", 2, "2010s", [])).state.movie_length, 2)

@route
def select_genre(state: State, genre: str = '')-> Page:
    '''
    This is how the Select Genre Page is displayed
    The user is prompted with buttons, and the one they click is stored in State
    Button for Comedy, Horror, Action, and Fantasy
    Args - state: current website state, genre: users selected genre
    Returns - A Page displaying the available genres and a button to continue to the next section: movie length
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

assert_equal(select_genre(State("", 1, "2020s", []), "Comedy").state.genre, "Comedy")
assert_equal(select_genre(State("", 2, "2010s", []), "Horror").state.genre, "Horror")

@route
def select_length(state: State, length: int = 0) -> Page:
    '''
    This is how the Select Length Page is displayed
    The user is prompted with buttons, and the one they click is stored in State
    Button for Under 90 mins, between 90-120 mins, over 120 mins
    Args - state: current website state, length: users selected length
    Returns - A Page displaying the available lengths and a button to continue to the next section: movie era
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

assert_equal(select_length(State("Comedy", 0, "2020s", []), 1).state.movie_length, 1)
assert_equal(select_length(State("Horror", 0, "2010s", []), 2).state.movie_length, 2)

@route
def select_era(state: State, era: str = '') -> Page:
    '''
    This is how the Select Era Page is displayed
    The user is prompted with buttons, and the one they click is stored in State
    Button for 90s, 00s, 10s, 20s
    Args - state: current website state, era: users selected era
    Returns - A Page displaying the available eras and a button to continue to the next section: get recommendations
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

assert_equal(select_era(State("Comedy", 1, "", []), "2020s").state.movie_era, "2020s")
assert_equal(select_era(State("Horror", 2, "", []), "2010s").state.movie_era, "2010s")

@route
def get_recommendations(state: State) -> Page:
    '''
    Matchs the users selected preferences with a specific movie from the dataset
    Every movie in movies is compared to the users preference for the perfect match, when a movie matches the recommendation preferences it will be added to the recommendations list
    Args - state: website with the users selected genre, movie length, and era
    Returns - results page displaying the matching movies
    '''
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

assert_equal(get_recommendations(State("Comedy", 1, "2020s", [])).state.recommendations, [Movie("Bad Trip", "Comedy", 84, "2020s")])
assert_equal(get_recommendations(State("Horror", 2, "2010s", [])).state.recommendations, [Movie("Get Out", "Horror", 104, "2010s")])

@route
def results(state: State) -> Page:
    '''
    Displays the users movie recommendation based off their previous selections
    Args - state: current website state including the list of recommended movies
    Returns - Page displaying the movie recommendation and a return home button
    '''
    return Page(state, [
        Header("Your Movie Recommendation"),
        Table(state.recommendations),
        Button("Return Home", "return_home")
    ])

assert_equal(results(State("Comedy", 1, "2020s", [])).state.genre, "Comedy")
assert_equal(results(State("Horror", 2, "2010s", [])).state.movie_era, "2010s")

@route
def return_home(state: State) -> Page:
    '''
    Resets the website state to original empty or 0 values 
    Args - state: current website state
    Returns - Page displaying the Movie Generator home page with base values
    '''
    state.genre = ""
    state.movie_length = 0
    state.movie_era = ""
    state.recommendations = []
    return index(state)

assert_equal(return_home(State("Comedy", 1, "2020s", [])).state, State("", 0, "", []))
assert_equal(return_home(State("Horror", 2, "2010s", [])).state, State("", 0, "", []))

start_server(State("", 0, "", []))
