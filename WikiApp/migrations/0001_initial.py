# Generated by Django 2.0.6 on 2019-03-13 14:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleSideContentModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SideTitle', models.CharField(max_length=200)),
                ('SideBody', models.TextField(max_length=200)),
                ('SidePicture', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='WikiArticleModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=200)),
                ('Body', models.TextField(max_length=1000)),
                ('Image', models.ImageField(upload_to='')),
                ('DateCreated', models.DateField(default=django.utils.timezone.now)),
                ('LastEditted', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='WikiEditorModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(max_length=200)),
                ('Password', models.CharField(max_length=300)),
                ('Email', models.EmailField(max_length=254)),
                ('ProfilePicture', models.ImageField(upload_to='')),
                ('Description', models.TextField(max_length=500)),
                ('Accountlink', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='wikiarticlemodel',
            name='User',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='WikiApp.WikiEditorModel'),
        ),
        migrations.AddField(
            model_name='articlesidecontentmodel',
            name='ArticleLink',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='WikiApp.WikiArticleModel'),
        ),
    ]
