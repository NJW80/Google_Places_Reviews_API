
import urllib
import urllib.request
import json

# A Google API key is needed to run the query
# To get one following the link: https://developers.google.com/places/web-service/get-api-key
api_key = 'xxx'


# Function to get place ID
def get_google_place_id(query):
    cleaned_query = query.replace(' ', '%20')
    url = 'https://maps.googleapis.com/maps/api/place/textsearch/json?query=' + cleaned_query + '&key=' + api_key
    response = urllib.request.urlopen(url).read().decode('utf8')
    data = json.loads(response)
    # Assumes the 1st Place ID is correct. Manual testing proved this to be correct. A more robust method would be
    # needed for more scaled usage
    return data['results'][0]['place_id']


# Function to process the reviews that come back from the API in the form of json data
def get_google_reviews(query):
    place_id = get_google_place_id(query)
    url = 'https://maps.googleapis.com/maps/api/place/details/json?placeid=' + place_id + '&key=' + api_key
    print(url)
    response = urllib.request.urlopen(url).read().decode('utf8')
    data = json.loads(response)
    print("{} has an overall rating of {}".format(query, data['result']['rating']))
    print()
    print("Here's what some people who went there thought:")
    print('\n')
    for review in data['result']['reviews']:
        print('Rating: {} - {} -  Review: {}'.format(review['rating'],review['relative_time_description'],review['text']))
        print('\n')



# Calling the functions requesting a users' input
get_google_reviews( input("What Bar/Restaurant do you want to search for?") )

# Some examples of directly passing the search query
# get_google_reviews('Mere Fitzrovia')
# get_google_place_id('Bar 61 Streatham')

