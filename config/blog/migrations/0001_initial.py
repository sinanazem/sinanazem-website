# Generated by Django 4.2.7 on 2023-12-01 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('abstract', models.TextField()),
                ('image', models.ImageField(upload_to='')),
                ('content', models.TextField()),
                ('status', models.CharField(choices=[('D', 'Draft'), ('P', 'Publish')], max_length=1)),
                ('publish', models.DateField(auto_now=True)),
                ('updatetime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
