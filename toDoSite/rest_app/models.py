from datetime import datetime
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.conf import settings
from django.dispatch import receiver
from django.utils import timezone
from rest_framework.authtoken.models import Token


#by convention you should use a singluar name for your class because it creates one instance
class ToDo(models.Model):
	text = models.CharField(max_length=250, unique=True)#unique makes it so that you can't repeat them
	timestamp = models.DateTimeField(default=datetime.now())
	completed = models.BooleanField(default=False)
	edited_date = models.DateTimeField(blank=True, null=True)

	def __str__(self):
		return self.text


	class Meta:
		ordering = ['completed', '-timestamp']

	def __str__(self):
		return self.text

	def save(self, *args, **kwargs):
		if not self.completed:
			self.edited_date = timezone.now()
		super(ToDo, self).save(*args, **kwargs)


# For newly created users
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
