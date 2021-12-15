# post_save = after saving a model
from django.db.models.signals import post_save
# user model
from django.contrib.auth.models import User
# signal documentations
from django.dispatch import receiver
from .models import Profile




@receiver(post_save,sender=User)
def create_profile(sender,instance,created,**kwargs):
    if created:
        print(instance)
        Profile.objects.create(user=instance)



@receiver(post_save,sender=User)
def save_profile(sender,instance,**kwargs):
    instance.profile.save()




# let say someone created a user but didnt created a profile
# so this finc will be called evertime  a user created so profile willbe created associated with the user
