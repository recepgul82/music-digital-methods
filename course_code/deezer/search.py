import requests
import pandas as pd


def search_deezer_tracks(query: str, limit: int = 25) -> dict:
    """
    Query the Deezer API for tracks matching a search string.

    Parameters
    ----------
    query : str
        Search term (artist name, genre, keyword).
    limit : int
        Number of results to retrieve.

    Returns
    -------
    dict
        Raw JSON response from Deezer API.
    """
    base_url = "https://api.deezer.com/search/track"
    params = {"q": query, "limit": limit}

    response = requests.get(base_url, params=params)
    response.raise_for_status()

    return response.json()


def search_deezer_artists(query: str, limit: int = 25) -> dict:
    """
    Query the Deezer API for artists matching a search string.

    Parameters
    ----------
    query : str
        Search term (artist name, keyword, country, etc.).
    limit : int
        Number of results to retrieve.

    Returns
    -------
    dict
        Raw JSON response from Deezer API.
    """
    base_url = "https://api.deezer.com/search/artist"
    params = {"q": query, "limit": limit}

    response = requests.get(base_url, params=params)
    response.raise_for_status()

    return response.json()


def search_deezer_albums(query: str, limit: int = 25) -> dict:
    """
    Query the Deezer API for albums matching a search string.

    Parameters
    ----------
    query : str
        Search term (album title, artist name, keyword).
    limit : int
        Number of results to retrieve.

    Returns
    -------
    dict
        Raw JSON response from Deezer API.
    """
    base_url = "https://api.deezer.com/search/album"

    params = {"q": query, "limit": limit}

    response = requests.get(base_url, params=params)
    response.raise_for_status()

    return response.json()


def get_country_chart_tracks(country_code: str = "tr", limit: int = 25) -> dict:
    """
    Retrieve top chart tracks for a given country from Deezer.

    Parameters
    ----------
    country_code : str
        ISO country code (e.g., "tr", "us", "fr").
    limit : int
        Number of tracks to retrieve.

    Returns
    -------
    dict
        Raw JSON response from Deezer API.
    """
    base_url = f"https://api.deezer.com/chart/{country_code}/tracks"

    params = {"limit": limit}

    response = requests.get(base_url, params=params)
    response.raise_for_status()

    return response.json()


def get_deezer_genres() -> pd.DataFrame:
    """
    Retrieve the full genre list from the Deezer API
    and return as a DataFrame.
    """
    url = "https://api.deezer.com/genre"

    response = requests.get(url)
    response.raise_for_status()

    data = response.json()

    records = []
    for item in data.get("data", []):
        records.append({"genre_id": item.get("id"), "genre_name": item.get("name")})

    return pd.DataFrame(records)
