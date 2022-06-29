from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill


# Generate image path
# def post_image_path(instance, filename):
#     # return f'posts/{instance.content}/{filename}'
#     return f'detail/{instance.content}/{instance.content}.jpg'

# Create your models here.
class BookBoardModel(models.Model):
    title = models.CharField(max_length=30, null=False)
    content = models.TextField()
    #to be updated after the sign up page

    pub_date= models.DateTimeField('date published', null=True)
    writer = models.CharField(max_length=20, null=True)
    image = models.ImageField(null=True, blank=True, upload_to='category_books_page/%Y/%m/%d/')

    def __str__(self):
        return self.title

    def summary(self):
        return self.content[:100]

    def publish(self):
        self.save()