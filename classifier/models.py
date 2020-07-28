from django.db import models
import datetime
from django.utils import timezone

## Think of model as object in OOP

class News(models.Model):
    news_text = models.CharField(max_length=1000)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.news_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Category(models.Model):
    ## Foreign Key of News Table
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    category = models.CharField(max_length=100)
    prob_score = models.FloatField(default=0)

    def __str__(self):
        return self.category
