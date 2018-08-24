from django.db import models
from datetime import datetime

# Create your models here.

#by convention you should use a singluar name for your class because it creates one instance
class ToDo(models.Model):
    to_do_text = models.CharField(max_length=250, unique=True)#unique makes it so that you can't repeat them
    created_Date = models.DateTimeField(default=datetime.now())
    completed = models.BooleanField(default=False)
    # once you have set up a class you have to run a migrations with python \manage.py makemigrations doDoApp. Once this is successful you should have a 0001_initial in yoru omigrations folder. After any changes to models you must make another migration. this creates instructions for migrating. python manage.py migrate then actually migrates things to the app.

    def __str__(self):
        return self.to_do_text
