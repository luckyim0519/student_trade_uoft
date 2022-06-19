# Generated by Django 4.0.5 on 2022-06-19 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup_page', '0005_account_delete_signupmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('username', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=50, primary_key=True, serialize=False, unique=True)),
                ('password', models.CharField(max_length=25)),
            ],
            options={
                'db_table': 'user',
            },
        ),
        migrations.DeleteModel(
            name='Account',
        ),
    ]
