from datetime import timezone

#import Notification as Notification
from django.db import models

class UserInfo(models.Model):
    username = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    per_dur = models.IntegerField(default=0)
    age = models.IntegerField(default=10)  #change default to 10 later
    start_date = models.DateField()
    end_date = models.DateField()
    missed_count = models.IntegerField(default=0)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name


class Questions(models.Model):
    username = models.CharField(max_length=50)
    ques = models.CharField(max_length=2000)
    ans = models.CharField(max_length=2000)

    #def add_notification(self, message):
       # notification = Notification(user=self.user, message=message)
        #notification.save

class FAQ(models.Model):
    quest = models.CharField(max_length=2000)
    answ = models.CharField(max_length=2000)


class Calorie(models.Model):
    food = models.CharField(max_length=100)
    cal = models.IntegerField(default=500)