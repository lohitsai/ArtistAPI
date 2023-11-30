from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from Artist.models import ArtistModel
from rest_framework.authtoken.models import Token


@receiver(post_save, sender=get_user_model())
def creating_artist(sender, instance, **kwargs):
    print("running")
    # attaching the user instance to a new Artist Instance
    artist = ArtistModel.objects.create(name=instance.first_name, userInstance=instance)
    artist.save()
    # Creating the Token for the user
    Token.objects.create(user=instance)
