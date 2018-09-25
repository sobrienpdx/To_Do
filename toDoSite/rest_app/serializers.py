from rest_framework import serializers
from .models import ToDo
from django.contrib.auth.models import User, Group

class ToDoSerializer(serializers.ModelSerializer):
	class Meta:
		model = ToDo
		fields = '__all__'
