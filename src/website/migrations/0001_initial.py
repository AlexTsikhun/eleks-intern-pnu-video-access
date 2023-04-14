# Generated by Django 4.2 on 2023-04-14 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_name', models.CharField(max_length=100)),
                ('brief_description', models.CharField(max_length=70)),
                ('video_genre', models.CharField(max_length=30)),
                ('username', models.CharField(max_length=20)),
                ('video_link', models.CharField(max_length=512)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
