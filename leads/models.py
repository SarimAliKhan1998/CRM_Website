from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    is_organizer = models.BooleanField(default=True)
    is_agent = models.BooleanField(default= False)



class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username    


class Lead(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    age = models.PositiveIntegerField()
    organisation = models.ForeignKey(UserProfile,  on_delete=models.CASCADE)
    agent = models.ForeignKey("Agent", blank=True, null= True,on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    organisation = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username



def post_user_created_signal(sender, instance, created, **kwargs):
    # print(instance, created)
    if created:
        UserProfile.objects.create(user = instance)

post_save.connect(post_user_created_signal, sender = User)