from bs4 import BeautifulSoup
import requests

def scrape_mal_data(anime_url):
    # Get the anime data from MAL
    response = requests.get(anime_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the title of the show
    title_element = soup.find('div', {'itemprop': 'name'})

    # Find the show's popularity
    popularity_element = soup.find('span', {'class': 'numbers popularity'})

    # Find the show's rating
    rating_element = soup.find('div', class_='score-label')

    # Initialize an empty dictionary to store the data
    anime_info = {}

    # Extract and store the title(Note: Switch from web scraping to Myanimelist's API)
    if title_element:
        h1_element = title_element.find('h1', {'class': 'title-name h1_bold_none'})
        if h1_element:
            strong_element = h1_element.find('strong')
            if strong_element:
                anime_info['title'] = strong_element.text.strip()
            else:
                anime_info['title'] = "Title not found"
        else:
            anime_info['title'] = "H1 element not found"
    else:
        anime_info['title'] = "Title element not found"

    # Extract and store the popularity
    if popularity_element:
        strong_element2 = popularity_element.find('strong')
        if strong_element2:
            anime_info['popularity'] = strong_element2.text.strip()
        else:
            anime_info['popularity'] = "Popularity element not found"
    else:
        anime_info['popularity'] = "Popularity element not found"

    # Extract and store the rating
    if rating_element:
        anime_info['rating'] = rating_element.text.strip()
    else:
        anime_info['rating'] = "Rating element not found"

    return anime_info

# Request these Anime URLs: Enstars, I7, Hypmic, Paralive
anime_urls = [
    'https://myanimelist.net/anime/32212/Ensemble_Stars',
    'https://myanimelist.net/anime/33899/IDOLiSH7',
    'https://myanimelist.net/anime/40803/Hypnosis_Mic__Division_Rap_Battle_-_Rhyme_Anima',
    'https://myanimelist.net/anime/51956/Paradox_Live_the_Animation',
]

# Scrape myanimelist for data
anime_data = [scrape_mal_data(url) for url in anime_urls]
