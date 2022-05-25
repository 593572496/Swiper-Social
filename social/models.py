from django.db import models


class Swiped(models.Model):  # 划过的记录表
    STATUS = (
        ('superlike', '超级喜欢'),
        ('like', '喜欢'),
        ('dislike', '不喜欢')
    )
    uid = models.IntegerField(verbose_name='滑动者的uid')
    sid = models.IntegerField(verbose_name='被滑动者的uid')
    status = models.CharField(max_length=9, verbose_name='滑动的类型', choices=STATUS)
    time = models.DateTimeField(auto_now_add=True)

    @classmethod
    def mark(cls, uid, sid, status):
        """标记一次滑动，由于这里没法使用某个实例对象去创建，所以采用类方法"""
        if status in ('superlike', 'like', 'dislike'):
            cls.objects.update_or_create(uid, sid, status)

    @classmethod
    def is_liked(cls, uid, sid):
        """检查uid喜欢的人是否喜欢过他"""
        return cls.objects.filter(uid=uid, sid=sid, status__in=('like', 'superlike')).exists()


class Friend(models.Model):
    uid = models.IntegerField()
    fid = models.IntegerField()

    # 成为好朋友
    @classmethod
    def become_friend(cls, uid, sid):
        uid, sid = (sid, uid) if uid > sid else (uid, sid)
        cls.objects.get_or_create(uid, sid)

    # 断交
    @classmethod
    def break_friend(cls, uid, sid):
        uid, sid = (sid, uid) if uid > sid else (uid, sid)
        try:
            cls.objects.get(uid=uid, fid=sid).delete()
        except cls.DoesNotExist:
            pass
