import datetime

from django.db.models import Q

from user.models import User
from social.models import Swiped, Friend


def get_rcmd_users(user):  # 根据登录用户的设置的交友特点进行用户匹配
    min_age = user.profile.min_age
    max_age = user.profile.max_age
    dating_sex = user.profile.dating_sex
    location = user.profile.location
    #
    now_year = datetime.date.today().year
    min_year = now_year - min_age
    max_year = now_year - max_age
    match_user = User.objects.filter(sex=dating_sex, location=location, birth_year__gte=max_year,
                                     birth_year__lte=min_year)  # filter无法直接使用属性，只能使用定义的字段进行过滤
    return match_user


def like_operation(user, sid):
    """喜欢一个用户"""
    Swiped.mark(user.id, sid, 'like')
    # 检查被滑动的用户是否喜欢过自己,如果喜欢过自己那么自动成为朋友
    if Swiped.is_liked(sid, user.id):
        Friend.become_friend(user.id, sid)
        return True
    else:
        return False


def superlike_operation(user, sid):
    """超级喜欢一个用户"""
    Swiped.mark(user.id, sid, 'superlike')
    # 检查被滑动的用户是否喜欢过自己,如果喜欢过自己那么自动成为朋友
    if Swiped.is_liked(sid, user.id):
        Friend.become_friend(user.id, sid)
        return True
    else:
        return False


def dislike_operation(user, sid):
    """不喜欢"""
    Swiped.mark(user.id, sid, 'dislike')


def rewind_operation(user, sid):
    """反悔,取消之前的所有状态，包括删除好友"""
    try:
        Swiped.objects.filter(uid=user.id, sid=sid).delete()  # 取消滑动记录
    except Swiped.DoesNotExist:
        pass
    else:
        Friend.break_friend(uid=user.id, sid=sid)  # 删除好友关系（else只有前面存在记录时才会执行）


def friends_operation(user):
    """查询自己的好友"""
    friends1 = Friend.objects.filter(uid=user.id)
    friends2 = Friend.objects.filter(fid=user.id)
    friend_id_group = []
    for friend in friends1:
        friend_id_group.append(friend.fid)
    for friend in friends2:
        friend_id_group.append(friend.uid)
    return User.objects.filter(id__in=friend_id_group).all()
