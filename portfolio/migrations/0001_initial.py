# Generated by Django 4.0 on 2021-12-30 21:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
        ('blog', '0010_alter_article_slug_alter_article_state_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('slug', models.CharField(max_length=120)),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('source_link', models.CharField(max_length=200, null=True)),
                ('demo_link', models.CharField(blank=True, max_length=200, null=True)),
                ('vote', models.IntegerField(default=1)),
                ('state', models.BooleanField(choices=[(False, 'Desactive'), (True, 'Active')], default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.profile')),
                ('tags', models.ManyToManyField(to='blog.Tag')),
            ],
        ),
    ]
