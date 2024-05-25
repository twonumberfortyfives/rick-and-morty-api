import requests

from characters.models import Characters
from rick_and_morty_api import settings


def scrape_characters() -> list[Characters]:
    next_url_to_scrape = settings.RICK_AND_MORTY_API_CHARACTERS_URL
    characters = []
    while next_url_to_scrape:
        characters_response = requests.get(next_url_to_scrape).json()
        for character in characters_response["results"]:
            characters.append(
                Characters(
                    api_id=character["id"],
                    name=character["name"],
                    status=character["status"],
                    species=character["species"],
                    gender=character["gender"],
                    image=character["image"],
                )
            )
        next_url_to_scrape = characters_response["info"]["next"]
    return characters


def save_characters(characters: list[Characters]) -> None:
    for character in characters:
        character.save()


def sync_characters_with_api() -> None:
    characters = scrape_characters()
    save_characters(characters)
