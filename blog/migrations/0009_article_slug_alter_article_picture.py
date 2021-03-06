# Generated by Django 4.0 on 2021-12-26 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_alter_article_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='slug',
            field=models.SlugField(max_length=255, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='picture',
            field=models.ImageField(null=True, upload_to='articles/'),
        ),
    ]
