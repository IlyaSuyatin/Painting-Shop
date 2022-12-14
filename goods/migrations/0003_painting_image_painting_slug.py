# Generated by Django 4.0.4 on 2022-07-08 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0002_alter_painting_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='painting',
            name='image',
            field=models.ImageField(default='hello', upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='painting',
            name='slug',
            field=models.SlugField(default='slug', unique=True),
            preserve_default=False,
        ),
    ]
