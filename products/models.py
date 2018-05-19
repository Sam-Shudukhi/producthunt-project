from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# Product class
class Product(models.Model):
# title
    title = models.CharField(max_length=100, unique=True)
# url
    url = models.TextField ()
# pub_date
    pub_date = models.DateTimeField()
# votes_total
    votes_total = models.IntegerField(default=1)
# image
    image = models.ImageField(upload_to='images/')
# icon
    icon = models.ImageField(upload_to='images/')
# body
    body = models.TextField()
# Person who submitted/found the product // delete products upon user account deletion
    hunter = models.ForeignKey(User, on_delete=models.CASCADE)

# pub_date_pretty
    def pub_date_pretty(self):
        return self.pub_date.strftime("%b %e, %Y")

# show titles in admin panel instead of blog objects
    def __str__(self):
        return self.title

# func to view a summary of blog post body (1st 100 chars)
    def summary(self):
        return self.body[:100]
