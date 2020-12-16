from django.db import models

#I am following directions in the Django for Beginners (3.1) book, by William S. Vincent - Hexx King

class Post(models.Model):
  title = models.CharField(max_length=64)
  author = models.ForeignKey(
    'auth.User',
    on_delete=models.CASCADE,
  )
  body = models.TextField()

  def __str__(self):
    return self.title
