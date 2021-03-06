# Generated by Django 2.0.6 on 2019-03-13 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WikiApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlesidecontentmodel',
            name='SideBody',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='articlesidecontentmodel',
            name='SidePicture',
            field=models.ImageField(upload_to='Side_Content_Images'),
        ),
        migrations.AlterField(
            model_name='wikiarticlemodel',
            name='Image',
            field=models.ImageField(upload_to='Article_Images'),
        ),
        migrations.AlterField(
            model_name='wikieditormodel',
            name='ProfilePicture',
            field=models.ImageField(upload_to='Profile_Pictures'),
        ),
    ]
