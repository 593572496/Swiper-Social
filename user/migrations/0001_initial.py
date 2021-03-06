# Generated by Django 4.0 on 2022-05-19 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=32, verbose_name='目标城市')),
                ('min_distance', models.IntegerField(default=1, verbose_name='最小距离(KM)')),
                ('max_distance', models.IntegerField(default=100, verbose_name='最大距离(KM)')),
                ('min_age', models.IntegerField(default=18, verbose_name='最小交友年龄')),
                ('max_age', models.IntegerField(default=45, verbose_name='最大交友年龄')),
                ('dating_sex', models.CharField(choices=[('M', '男'), ('F', '女')], default=8, max_length=8, verbose_name='交友性别')),
                ('vibration', models.BooleanField(default=True, verbose_name='是否开启振动')),
                ('only_matche', models.BooleanField(default=True, verbose_name='不让匹配我的人查看我的相册')),
                ('auto_play', models.BooleanField(default=True, verbose_name='是否自动播放视频')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=16, unique=True)),
                ('phone', models.CharField(max_length=16, unique=True)),
                ('sex', models.CharField(choices=[('M', '男'), ('F', '女')], max_length=8)),
                ('birth_year', models.IntegerField()),
                ('birth_month', models.IntegerField()),
                ('birth_day', models.IntegerField()),
                ('avatar', models.CharField(max_length=256)),
                ('location', models.CharField(max_length=32)),
            ],
        ),
    ]
