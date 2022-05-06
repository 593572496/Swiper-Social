from django.db import models
import datetime


class User(models.Model):
    SEX = (('M', '男'), ('F', '女'))
    nickname = models.CharField(max_length=16, unique=True)
    phone = models.CharField(max_length=16, unique=True)
    sex = models.CharField(choices=SEX, max_length=8)
    birth_year = models.IntegerField()
    birth_month = models.IntegerField()
    birth_day = models.IntegerField()
    avatar = models.CharField(max_length=256)  # 个人形象,头像链接
    location = models.CharField(max_length=32)

    @property
    def age(self):
        today = datetime.date.today()
        birth_day = datetime.date(self.birth_year, self.birth_month, self.birth_day)
        return (today - birth_day).days // 365
