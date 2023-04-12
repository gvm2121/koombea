from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class MainWebs(models.Model):
    user = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    name = models.CharField(blank=True,null=True,default="in progress")
    url = models.CharField(blank=True,null=True)
    total_links = models.CharField(blank=True,null=True, default="in progress")

    def __str__(self):
        return self.name

class DetailsWeb(models.Model):
    web_parent = models.ForeignKey(MainWebs, on_delete=models.DO_NOTHING)
    name_detail = models.CharField(blank=True,null=True)
    link_detail = models.CharField(blank=True,null=True)

    def __str__(self):
        return self.name_detail