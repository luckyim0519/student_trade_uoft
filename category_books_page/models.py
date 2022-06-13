from django.db import models

# Create your models here.
class BookBoardModel(models.Model):
    title = models.CharField(max_length=30, null=False)
    content = models.TextField()
    #to be updated after the sign up page
    pub_date= models.DateTimeField('date published')
    writer = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.title
