from django.db import models
from django.contrib.auth.models import User

SHORT_TEXT_LEN = 300

class Article(models.Model):
    title = models.CharField(max_length = 200)
    text = models.TextField()
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    def __str__(self):
        return self.title

    def get_short_text(self):
        if len(self.text) > SHORT_TEXT_LEN:
            return self.text[:SHORT_TEXT_LEN]
        else:
            return self.text