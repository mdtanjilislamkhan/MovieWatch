from django.test import TestCase

# Create your tests here.
'''queryset1=Movie.objects.all()
        for obj in queryset1:
            url = f"https://moviesdatabase.p.rapidapi.com/titles/{obj.imdb_id}/ratings"
            headers = {
                "X-RapidAPI-Key": "6b32103fa2msh39f193544b02f1fp185db3jsn6623e4eac535",
                "X-RapidAPI-Host": "moviesdatabase.p.rapidapi.com"
            }
            response = requests.request("GET", url, headers=headers)
            data = response.json()
            movie=Movie.objects.get(imdb_id=obj.imdb_id)
            print(movie.title,data['results']['averageRating'])
            movie.averageRating=data['results']['averageRating']
            movie.save()
        print("done")'''

'''import requests
from bs4 import BeautifulSoup

def get_website_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        # Perform data extraction based on the website's HTML structure
        # For example, let's assume we want to extract the titles of all <h1> tags:
        titles = [h1.text for h1 in soup.find_all('h1')]
        return titles
    else:
        return None

# Example usage
website_url = 'https://www.example.com'
data = get_website_data(website_url)
if data:
    for title in data:
        print(title)
else:
    print('Failed to retrieve data from the website.')
'''