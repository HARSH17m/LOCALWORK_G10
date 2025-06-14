# Generated by Django 5.2.3 on 2025-06-13 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='post_images/')),
                ('title', models.TextField(blank=True, max_length=255)),
                ('context', models.TextField(blank=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
    ]
