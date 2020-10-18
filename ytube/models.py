from django.db import models

# Create your models here.
class sentiment(models.Model):

    input_sentiment = models.CharField(max_length=500)

    def __str__(self):
        return '{}'.format(self.input_sentiment)