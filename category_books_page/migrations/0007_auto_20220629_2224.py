# Generated by Django 2.2.5 on 2022-06-29 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category_books_page', '0006_alter_bookboardmodel_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookboardmodel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='category_books_page/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='bookboardmodel',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
