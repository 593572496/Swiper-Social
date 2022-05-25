from django.db import models
import datetime
from lib.orm import ModelMixin


class User(models.Model):
    """用户个人信息"""
    SEX = (('M', '男'), ('F', '女'))
    nickname = models.CharField(max_length=16, unique=True)
    phone = models.CharField(max_length=16, unique=True)
    sex = models.CharField(choices=SEX, max_length=8)
    birth_year = models.IntegerField(default=2000)
    birth_month = models.IntegerField(default=1)
    birth_day = models.IntegerField(default=1)
    avatar = models.CharField(max_length=256)  # 个人形象,头像链接
    location = models.CharField(max_length=32)

    @property
    def age(self):
        today = datetime.date.today()
        birth_day = datetime.date(self.birth_year, self.birth_month, self.birth_day)
        return (today - birth_day).days // 365

    @property
    def profile(self):
        """用户配置项，不使用外键实现一对一"""
        """判断对象中是否有my_profile，如果没有就动态将my_profile加到对象上"""
        """效果：self.my_profile.xxxx时除了第一次回会执行my_profile, created = Profile.objects.get_or_create(pk=self.id)
        后续执行都是取的对象的属性值，不用每次都去数据库,类似懒加载机制"""
        # if not hasattr(self,'my_profile')
        if 'my_profile' not in self.__dict__:
            my_profile, _ = Profile.objects.get_or_create(pk=self.id)  # 返回对象和创建结果
            self.my_profile = my_profile
        return self.my_profile

    def to_dict(self):
        return {
            'id': self.id,
            'nickname': self.nickname,
            'phone': self.phone,
            'sex': self.sex,
            'avatar': self.avatar,
            'location': self.location,
            'age': self.age
        }


class Profile(models.Model, ModelMixin):
    """用户配置项"""
    SEX = (('M', '男'), ('F', '女'))
    location = models.CharField(max_length=32, verbose_name='目标城市')
    min_distance = models.IntegerField(verbose_name='最小距离(KM)', default=1)
    max_distance = models.IntegerField(verbose_name='最大距离(KM)', default=100)
    min_age = models.IntegerField(default=18, verbose_name='最小交友年龄')
    max_age = models.IntegerField(default=45, verbose_name='最大交友年龄')
    dating_sex = models.CharField(choices=SEX, default='F', verbose_name='交友性别', max_length=8)
    vibration = models.BooleanField(default=True, verbose_name='是否开启振动')
    only_match = models.BooleanField(default=True, verbose_name='不让匹配我的人查看我的相册')
    auto_play = models.BooleanField(default=True, verbose_name='是否自动播放视频')
