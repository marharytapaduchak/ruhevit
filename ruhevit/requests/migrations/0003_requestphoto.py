# Generated by Django 5.2 on 2025-04-14 13:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('requests', '0002_requesthistory_comment_requesthistory_photo_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='RequestPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='request_photos/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('history', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='requests.requesthistory')),
            ],
        ),
    ]
