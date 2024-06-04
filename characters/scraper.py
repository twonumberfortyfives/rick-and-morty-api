from urllib.parse import urlparse

import requests
import socket
from django.db import IntegrityError
from characters.models import Characters
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def check_hostname_resolution(url: str) -> bool:
    try:
        # Extract hostname from URL
        parsed_url = urlparse(url)
        hostname = parsed_url.hostname

        # Check if the hostname resolves
        socket.getaddrinfo(hostname, None)
        return True
    except socket.gaierror:
        return False


def scrape_characters() -> list[Characters]:
    next_url_to_scrape = "https://rickandmortyapi.com/api/character"
    if not check_hostname_resolution(next_url_to_scrape):
        print("Hostname could not be resolved.")
        return []

    characters = []
    while next_url_to_scrape:
        response = requests.get(next_url_to_scrape)
        response.raise_for_status()  # Raises HTTPError for bad responses
        characters_response = response.json()
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
        try:
            character.save()
        except IntegrityError:
            print(
                f"Character with api_id {character.api_id} already exists in database"
            )


def sync_characters_with_api() -> None:
    characters = scrape_characters()
    save_characters(characters)
