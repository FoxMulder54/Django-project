# Generated by Django 4.0 on 2021-12-30 21:19

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('name', models.CharField(max_length=80)),
                ('username', models.CharField(blank=True, max_length=80, null=True, unique=True)),
                ('email', models.EmailField(blank=True, max_length=120, null=True, unique=True)),
                ('head_line', models.CharField(blank=True, max_length=200, null=True)),
                ('about_as', models.TextField(null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('resume_link', models.CharField(blank=True, max_length=200, null=True)),
                ('linkden_link', models.CharField(blank=True, max_length=200, null=True)),
                ('facebook_link', models.CharField(blank=True, max_length=200, null=True)),
                ('website_link', models.CharField(blank=True, max_length=200, null=True)),
                ('youtub_link', models.CharField(blank=True, max_length=200, null=True)),
                ('state', models.BooleanField(choices=[(False, 'Desactive'), (True, 'Active')], default=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
    ]