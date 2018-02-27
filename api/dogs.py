import requests
import random

def main():

    breeds = requests.get("https://dog.ceo/api/breeds/list/all")
    if breeds.status_code != requests.codes.ok:
        breeds.raise_for_status()
    data = breeds.json().get("message")
    breed_name = random.choice(list(data.keys()))
    print("The breed you got was %s" % breed_name)

    picture = requests.get("https://dog.ceo/api/breed/%s/images/random" % breed_name)
    if picture.status_code != requests.codes.ok:
        picture.raise_for_status()
    p_data = picture.json().get("message")
    print("Visit %s to see a picture of this dog" % p_data)

if __name__ == '__main__':
    main()