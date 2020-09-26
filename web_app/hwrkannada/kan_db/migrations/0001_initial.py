# Generated by Django 3.0 on 2019-12-03 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='KanDB',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kannada', models.CharField(max_length=50)),
                ('eng', models.CharField(max_length=50)),
                ('mis', models.CharField(max_length=50)),
                ('freq', models.IntegerField()),
                ('comp', models.IntegerField()),
                ('aud', models.FileField(upload_to='audio')),
                ('saud', models.FileField(upload_to='snail_audio')),
                ('img', models.ImageField(upload_to='image')),
            ],
        ),
    ]