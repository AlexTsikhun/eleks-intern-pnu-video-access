from django.db import models

class Record(models.Model):
	video_name = models.CharField(max_length=100)
	brief_description =  models.CharField(max_length=70)
	video_genre =  models.CharField(max_length=30)
	username = models.CharField(max_length=150)
	video_link =  models.CharField(max_length=512)
	created_at = models.DateTimeField(auto_now_add=True)


	def __str__(self):
		return(f"{self.video_name} {self.username}")
