from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill


# Generate image path
def post_image_path(instance, filename):
    # return f'posts/{instance.content}/{filename}'
    return f'category_books_page/detail/{instance.writer}/{filename}'

# Create your models here.
class BookBoardModel(models.Model):
    title = models.CharField(max_length=30, null=False)
    content = models.TextField()
    pub_date= models.DateTimeField('date published', null=True)
    # to be updated after the sign up page
    writer = models.CharField(max_length=20, null=True)
    image = ProcessedImageField(
        null=True,
        blank=True,
        upload_to=post_image_path,
        processors=[ResizeToFill(300, 300)],
        format='JPEG',
        options={'quality': 90},
    )

    def __str__(self):
        return self.title

    def summary(self):
        return self.content[:100]

    def publish(self):
        self.save()