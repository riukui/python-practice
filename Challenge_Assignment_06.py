import requests
import json

api_url = "https://nomad-movies.nomadcoders.workers.dev/movies/"

movie_ids = [
    238, 680, 550, 185, 641, 515042, 152532, 120467, 872585, 906126, 840430
]

for movie_id in movie_ids:
    url = f"{api_url}{movie_id}"
    response = requests.get(url)
    data = response.json()
    print(f"title : {data['title']}")
    print(f"overview : {data['overview']}")
    print(f"vote_average : {data['vote_average']}")
    print("---------------------------------")
