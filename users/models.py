from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.

# profile user for image
class Profile(models.Model):
    # this is has onetoone realtion which means user can oly have one profile
    # and a profile can only have user
    # and you can call user.profile.get() like that
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    # image field
    image = models.ImageField(default='helmet-1.png', upload_to='photos', null=True, blank=True)


    def __str__(self):
        return f'{self.user.username} profile'

    # built in models.Model save func
    # we just want to resize smage

        # get the save func from built in
    # def save(self, *args, **kwargs):
    #     super(Profile, self).save(*args, **kwargs)
    #     # then resize and save it
    #     if self.image:
    #         img = Image.open(self.image.path)
    #         if img.height>300 or img.width >300:
    #             output_size = (300,300)
    #             img.thumbnail(output_size)
    #             img.save(self.image.path)
