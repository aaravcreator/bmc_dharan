# Generated by Django 4.2.3 on 2023-07-26 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_socialplatform'),
    ]

    operations = [
        migrations.AddField(
            model_name='hero',
            name='hero_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
