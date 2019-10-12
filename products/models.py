from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    title=models.CharField(max_length=200)
    pub_date=models.DateTimeField()
    url=models.TextField()
    body=models.TextField(default='000000',editable=True)
    image=models.ImageField(upload_to='images/')
    icon=models.ImageField(upload_to='images/')
    votes_total=models.IntegerField(default=1)
    hunter=models.ForeignKey(User,on_delete=models.CASCADE)


    def __str__(self):
        return self.title
    def summary(self):
        return self.body[:100]
