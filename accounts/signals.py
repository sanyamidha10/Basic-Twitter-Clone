from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import profile

@receiver(post_save, sender=User)
def post_save_create_profile_receiver(sender, instance, created, **kwargs):
    if created:
            profile.objects.create(user=instance)
            print('user profile is created')
    else:
        try:
            userprofile = profile.objects.get(user=instance)
            userprofile.save()
        except:
            #create the user profile if not exist:
            userprofile = profile.objects.create(user=instance)