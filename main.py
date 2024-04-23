from datetime import datetime
import random


class Movie:
    def __init__(self, title: str, release_date: int, genre: str):
        self.title = title
        self.release_date = release_date
        self.genre = genre
        self.plays_count = 0

    def __str__(self):
        return f"{self.title} ({self.release_date})"

    def play(self):
        self.plays_count += 1


class MovieSeries(Movie):
    def __init__(self, seasons: dict, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.seasons = seasons

    def __str__(self):
        return f"{self.title} ({self.release_date})"

    def list_all_episodes(self):
        seasons = []
        for season, episodes in self.seasons.items():
            for episode in episodes:
                seasons.append(f"S{season:02d}E{episode:02d}")

        return seasons


def get_movies(films: list[Movie]) -> list[Movie]:
    return [film for film in films if not isinstance(film, MovieSeries)]


def get_series(films: list[Movie]) -> list[MovieSeries]:
    return [film for film in films if isinstance(film, MovieSeries)]


def search(films: list[Movie], search_query: str) -> Movie | None:
    for film in films:
        if search_query in film.title:
            return film
    return None


def generate_views(films: list[Movie]) -> None:
    film = random.choice(films)
    film.plays_count = random.randint(1, 100)


def top_titles(films: list[Movie], content_type=None) -> list[Movie]:
    if content_type == "movies":
        films = get_movies(films)
    elif content_type == "series":
        films = get_series(films)

    top_films = sorted(films, key=lambda film: film.plays_count, reverse=True)

    return top_films[:3]

TODAY = datetime.today().strftime('%d.%m.%Y')


def run_generate_views(films: list[Movie], times: int) -> None:
    for _ in range(times):
        generate_views(films)


def main() -> None:
    films = [
        Movie(title="Terminator", release_date=1984, genre="Action"),
        Movie(title="Rambo", release_date=1982, genre="Action"),
        Movie(title="Nie lubię poniedziałku", release_date=1971, genre="Comedy"),
        Movie(title="Brunet wieczorową porą", release_date=1976, genre="Comedy"),
        MovieSeries(title="Alternatywy 4", release_date=1986, genre="Comedy", seasons={1: [1, 2, 3, 4]}),
        MovieSeries(title="Trailer park boys", release_date=2001, genre="Sitcom/Comedy", seasons={1: [1, 2], 2: [1, 2], 3: [1, 2]}),
        MovieSeries(title="The Office", release_date=2005, genre="Sitcom/Comedy", seasons={1: [1, 2, 3], 2: [1, 2, 3]}),
    ]

    run_generate_views(films, 10)


    print(f"Najbardziej popularne filmy i seriale w dniu {TODAY} to:\n")
    for film in top_titles(films):
        print(f"\t  *  {film} - {film.plays_count} plays")


if __name__ == "__main__":
    main()