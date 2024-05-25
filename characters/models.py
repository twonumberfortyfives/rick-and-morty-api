from django.db import models


class Characters(models.Model):
    class StatusChoices(models.TextChoices):
        ALIVE = "Alive"
        DEAD = "Dead"
        UNKNOWN = "Unknown"

    class GenderChoices(models.TextChoices):
        FEMALE = "Female"
        MALE = "Male"
        GENDERLESS = "Genderless"
        UNKNOWN = "Unknown"

    api_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=100)
    status = models.CharField(
        choices=StatusChoices.choices,
        default=StatusChoices.UNKNOWN,
        max_length=100,
    )
    species = models.CharField(max_length=255)
    gender = models.CharField(
        choices=GenderChoices.choices,
        default=GenderChoices.UNKNOWN,
        max_length=100,
    )
    image = models.ImageField(upload_to="", max_length=255, unique=True)

    class Meta:
        verbose_name_plural = "Characters"
        verbose_name = "Character"

    def __str__(self):
        return self.name
