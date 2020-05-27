# Generated by Django 2.2.12 on 2020-05-18 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50, verbose_name='书名')),
                ('price', models.FloatField(default=0, verbose_name='价格')),
                ('cover', models.ImageField(default='img/default.png', upload_to='upload', verbose_name='封面')),
                ('introduction', models.TextField(blank=True, default='', verbose_name='介绍')),
                ('url', models.URLField(blank=True, default='', verbose_name='URL')),
                ('publish', models.CharField(blank=True, default='', max_length=50, verbose_name='出版社')),
                ('rating', models.CharField(default='0', max_length=5, verbose_name='评分')),
            ],
            options={
                'verbose_name_plural': '图书管理',
                'verbose_name': '图书管理',
            },
        ),
        migrations.CreateModel(
            name='hits',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.IntegerField(default=0)),
                ('bookid', models.IntegerField(default=0)),
                ('hitnum', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name_plural': '点击量',
                'verbose_name': '点击量',
            },
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(default='admin', max_length=6)),
            ],
            options={
                'verbose_name_plural': '用户管理',
                'verbose_name': '用户管理',
            },
        ),
    ]
