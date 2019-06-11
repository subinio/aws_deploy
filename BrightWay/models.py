from django.db import models

# Create your models here.

class Cs(models.Model):

    name = models.TextField()
    x = models.FloatField()
    y = models.FloatField()
    distinct = models.TextField(null = True)
    objects = models.Manager()
    def __str__(self):
        return self.name


class Fs(models.Model):
    name = models.TextField()
    x = models.FloatField()
    y = models.FloatField()
    distinct = models.TextField(null = True)
    time = models.TextField(null =True)
    objects = models.Manager()
    def __str__(self):
        return self.name
        
class Os(models.Model):
    name = models.TextField()
    x = models.FloatField()
    y = models.FloatField()
    distinct = models.TextField(null = True)
    objects = models.Manager()
    def __str__(self):
        return self.name

class Dong(models.Model):
    distinct = models.TextField()
    x = models.FloatField()
    y = models.FloatField()
    objects  = models.Manager()
    def __str__(self):
        return self.distinct

class Childuser(models.Model):
    UserName = models.TextField()
    UserID = models.TextField()
    UserPW = models.TextField()
    
    UserFlag = models.TextField(null = True)
    objects = models.Manager()

    def __str__(self):
        return self.UserName

class Parentuser(models.Model):
    UserName = models.TextField()
    UserID = models.TextField()
    UserPW = models.TextField()
    UserFlag = models.TextField()
    UserChild1Name = models.TextField(null = True)
    UserChild1ID = models.TextField(null = True)
    objects = models.Manager()

    def __str__(self):
        return self.UserName