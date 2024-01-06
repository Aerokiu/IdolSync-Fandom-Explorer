import requests

def scrape_mal_data(anime_url):
   
    response = requests.get(anime_url)

  
    if response.status_code == 200:
        # Parse the JSON data
        data = response.json()

        # Extract the desired information
        anime_data = data.get('data', [])
        if anime_data:
            anime_data = anime_data[0] 

            title = anime_data.get('title', 'Title not found')
            popularity = anime_data.get('popularity', 'Popularity not found')
            score = anime_data.get('score', 'Score not found')

            # Create a dictionary to store the data
            anime_info = {

                'title': title,
                'popularity': popularity,
                'score' : score
            }

            return anime_info
        else:
            print("Error: 'data' field not found in the response.")
    else:
        print(f"Error: {response.status_code}")

    return None

# Request these Anime APIs: Enstars, I7, Hypmic, Paralive
anime_apis = [
    'https://api.jikan.moe/v4/anime?q=Ensemble%20Stars&sfw',
    'https://api.jikan.moe/v4/anime?q=idolish7%20&sfw',
    'https://api.jikan.moe/v4/anime?q=hypnosis%20mic&sfw',
    'https://api.jikan.moe/v4/anime?q=paradox%20live&sfw',
]

# Scrape MyAnimeList for data
anime_data = [scrape_mal_data(api) for api in anime_apis]

# Data display test
#for data in anime_data:
    #print(data)
