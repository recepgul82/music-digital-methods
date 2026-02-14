import pandas as pd


def parse_tracks_to_dataframe(json_data: dict) -> pd.DataFrame:
    """
    Convert Deezer JSON track results into a structured DataFrame.
    """
    records = []

    for item in json_data.get("data", []):
        records.append(
            {
                "track_id": item.get("id"),
                "track_title": item.get("title"),
                "duration_sec": item.get("duration"),
                "rank": item.get("rank"),
                "artist_name": item.get("artist", {}).get("name"),
                "album_title": item.get("album", {}).get("title"),
            }
        )

    df = pd.DataFrame(records)
    return df


def parse_artists_to_dataframe(json_data: dict) -> pd.DataFrame:
    """
    Convert Deezer artist search JSON results into a structured DataFrame.

    Parameters
    ----------
    json_data : dict
        Raw JSON response returned by the Deezer API.

    Returns
    -------
    pd.DataFrame
        DataFrame containing selected artist-level features.
    """
    records = []

    for item in json_data.get("data", []):
        records.append(
            {
                "artist_id": item.get("id"),
                "artist_name": item.get("name"),
                "nb_albums": item.get("nb_album"),
                "nb_fans": item.get("nb_fan"),
                "radio": item.get("radio"),
                "tracklist_url": item.get("tracklist"),
            }
        )

    df = pd.DataFrame(records)

    # Ensure numeric columns are correctly typed
    numeric_cols = ["nb_albums", "nb_fans"]
    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    return df


def parse_albums_to_dataframe(json_data: dict) -> pd.DataFrame:
    """
    Convert Deezer album search JSON results into a structured DataFrame.

    Parameters
    ----------
    json_data : dict
        Raw JSON response returned by the Deezer API.

    Returns
    -------
    pd.DataFrame
        DataFrame containing selected album-level features.
    """
    records = []

    for item in json_data.get("data", []):
        artist = item.get("artist", {})

        records.append(
            {
                "album_id": item.get("id"),
                "album_title": item.get("title"),
                "release_date": item.get("release_date"),
                "nb_tracks": item.get("nb_tracks"),
                "artist_id": artist.get("id"),
                "artist_name": artist.get("name"),
                "record_type": item.get("record_type"),  # album, single, etc.
                "explicit_lyrics": item.get("explicit_lyrics"),
            }
        )

    df = pd.DataFrame(records)

    # Ensure numeric columns are correctly typed
    numeric_cols = ["nb_tracks"]
    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    return df
