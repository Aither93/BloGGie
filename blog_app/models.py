from django.db import models

# Create your models here.
class Blog(models.Model):
	title = models.CharField(max_length = 332)
	content = models.TextField()
	date_added = models.DateTimeField(auto_now_add = True)
