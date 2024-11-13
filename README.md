
# StreamVault

StreamVault is a python web application that allows users to search for movies and see an overview of them (genre, runtime, plot, actors, etc.) Similar to IMdB, however StreamVault also gives you the ability to view the available streaming platforms for the films.



## Features

- Create accounts
- Add movies to users' favorite/watch later list
- Watch the official movie trailer
- See the available streaming platforms (buy, rent, and or free)
- Popular List, which contains movies that are currently trending
- Top-Rated List, which contains the highest rated movies of all time  


## Prerequisites

- The Open Movie Database(OMDb) API Key
- The Movie Database(TMDB) API
## Run Locally

Clone the project

```bash
  git clone https://github.com/NateFox8/StreamVault.git
```

Go to the project directory

```bash
  cd StreamVault
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Change API Keys in 'util.py' module

```bash
  # change value to your TMDB api key
  tmdb.API_KEY = TMDB_KEY

  # change value to your OMDB api key
  OMDB_API_KEY = OMDB_KEY
```

Start the flask server

```bash
  python app.py
```


## Authors

- [@NateFox8](https://github.com/NateFox8)


## Acknowledgements


 - [The Open Movie Database(OMDb) API Documentation](https://www.omdbapi.com/)
 - [The Movie Database(TMDB) API Documentation](https://developer.themoviedb.org/reference/intro/getting-started)

