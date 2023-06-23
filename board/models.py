
from django.db import models
from django.contrib.auth.models import User, Group
from django.urls import reverse

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Post(models.Model):
    TANKS = "TK"
    HILS = "HL"
    DD = "DD"
    TRADES = "TD"
    GUILDMASTERS = "GM"
    QUAESTGILDERS = "QG"
    SMITHES = "SM"
    TANNERS = "TN"
    HERBMAKERS = "HM"
    WIZARDS = "WZ"

    CATEGORY_CHOICES = [
        (TANKS, 'Tanks'),
        (HILS, 'Hils'),
        (DD, 'DD'),
        (TRADES, 'Trades'),
        (GUILDMASTERS, 'Gildmasters'),
        (QUAESTGILDERS, 'Quaestgilders'),
        (SMITHES, 'Smitses'),
        (TANNERS, 'Tanners'),
        (HERBMAKERS, 'Herbmakers'),
        (WIZARDS, 'Wizards')
    ]

    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.CharField(max_length=2, choices=CATEGORY_CHOICES)
    post_time_in = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    post_text = models.TextField()

    def __str__(self):
        return f'{self.title.title()}'

    def get_absolute_url(self):
        return reverse('news_detail', args=[str(self.id)])


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_text = models.TextField()
    approved = models.BooleanField(default=False)



