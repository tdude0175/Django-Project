# Generated by Django 2.0.6 on 2019-03-15 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WikiApp', '0009_auto_20190314_1512'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wikiarticlemodel',
            name='Body',
            field=models.TextField(max_length=2500),
        ),
    ]
