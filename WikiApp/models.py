from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class WikiEditorModel(models.Model):
    Username = models.CharField(max_length=200)
    Password = models.CharField(max_length=300)
    Email = models.EmailField()
    ProfilePicture = models.ImageField()
    Description = models.TextField(max_length=500)
    Accountlink = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.Username


class WikiArticleModel(models.Model):
    Title = models.CharField(max_length=200)
    Body = models.TextField(max_length=1000)
    Image = models.ImageField()
    DateCreated = models.DateField(default=timezone.now)
    LastEditted = models.DateTimeField(default=timezone.now)
    User = models.ForeignKey(WikiEditorModel, on_delete=models.PROTECT)

    def __str__(self):
        return self.Title

class ArticleSideContentModel(models.Model):
    SideTitle = models.CharField(max_length=200)
    SideBody = models.TextField(max_length=200)
    SidePicture = models.ImageField()
    ArticleLink = models.ForeignKey(WikiArticleModel,on_delete=models.PROTECT)

    def __str__(self):
        return self.SideTitle
