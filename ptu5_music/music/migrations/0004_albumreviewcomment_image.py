# Generated by Django 4.1.3 on 2022-11-28 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_alter_albumreviewcomment_album_review_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='albumreviewcomment',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='user_images/', verbose_name='image'),
        ),
    ]