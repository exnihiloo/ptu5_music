# Generated by Django 4.1.3 on 2022-11-28 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0004_albumreviewcomment_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='albumreview',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='user_images/', verbose_name='image'),
        ),
    ]
