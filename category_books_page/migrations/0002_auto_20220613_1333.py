# Generated by Django 2.2 on 2022-06-13 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category_books_page', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookboardmodel',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]