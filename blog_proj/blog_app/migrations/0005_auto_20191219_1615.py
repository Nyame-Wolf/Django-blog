# Generated by Django 2.2.7 on 2019-12-19 16:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0004_post_tags'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-date_posted']},
        ),
    ]
