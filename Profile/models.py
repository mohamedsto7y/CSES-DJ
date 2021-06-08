from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.utils.text import slugify
# Create your models here.
class profile(models.Model):
    user=models.ForeignKey(User,related_name='profile',on_delete=models.CASCADE)
    first_name=models.CharField(max_length=10)
    last_name=models.CharField(max_length=10)
    email=models.EmailField(max_length=20)
    email_verification=models.BooleanField(default=False)
    telegram_code=models.CharField(max_length=10)
    telegram_id=models.IntegerField(default=0)
    user_photo=models.ImageField(upload_to='photo/',default='')
    slug=models.SlugField(default='')
    # grades
    @receiver(post_save,sender=User)
    def create_profle(sender,instance,created,**kwargs):
        if created:
            profile.objects.create(user=instance)
    def __str__(self):
        return str(self.user)
    def save(self, *args, **kwargs):
       if not self.slug:
           self.slug=slugify(self.user)    
       super(profile, self).save(*args, **kwargs) # Call the real save() method