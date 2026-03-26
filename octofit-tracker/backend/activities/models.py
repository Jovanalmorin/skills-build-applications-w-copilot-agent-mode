from django.db import models
from django.contrib.auth.models import User

class Activity(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	type = models.CharField(max_length=50)
	duration = models.FloatField()
	distance = models.FloatField(null=True, blank=True)
	timestamp = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"{self.user.username} - {self.type} ({self.duration} min)"
