from django.urls import path

from characters import views


app_name = "characters"

urlpatterns = [
    path("characters/random/", views.get_random_character, name="random_character"),
    path("characters/", views.CharacterListView.as_view(), name="character_list"),
]
