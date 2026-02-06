import pandas as pd


def fetch_playlist_tracks(sp, playlist_id, limit=100):
    """
    Returns a DataFrame with basic metadata + audio features.
    """

    tracks = []
    results = sp.playlist_items(
        playlist_id, limit=min(limit, 100), additional_types=["track"]
    )

    while results and len(tracks) < limit:
        for item in results["items"]:
            track = item.get("track")
            if track is None:
                continue

            tracks.append(
                {
                    "track_id": track["id"],
                    "track_name": track["name"],
                    "artist": ", ".join(a["name"] for a in track["artists"]),
                    "album": track["album"]["name"],
                    "release_date": track["album"]["release_date"],
                    "release_date_precision": track["album"]["release_date_precision"],
                    "duration": track["duration_ms"] / 3600,
                    "popularity": track["popularity"],
                }
            )

            if len(tracks) >= limit:
                break

        results = sp.next(results) if results["next"] else None

    df = pd.DataFrame(tracks)

    return df
