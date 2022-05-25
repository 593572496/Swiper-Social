from django.shortcuts import render
from lib.http import render_json
from social.logic import get_rcmd_users, like_operation, superlike_operation, dislike_operation, rewind_operation, \
    friends_operation


def get_users(request):
    """获取推荐列表"""
    group = int(request.GET.get('group_num', 0))
    start = group * 5
    end = start + 5
    users = get_rcmd_users(request.user)[start:end]
    data = [use.to_dict() for use in users]
    return render_json(data)


def like(request):
    """喜欢"""
    sid = request.POST.get('sdi')
    is_become_friend = like_operation(request.user, sid)
    return render_json({'is_become_friend': is_become_friend})


def superlike(request):
    """超级喜欢"""
    sid = request.POST.get('sdi')
    is_become_friend = superlike_operation(request.user, sid)
    return render_json({'is_become_friend': is_become_friend})


def dislike(request):
    """不喜欢"""
    sid = request.POST.get('sdi')
    dislike_operation(request.user, sid)
    return render_json(None)


def rewind(request):
    """反悔"""
    sid = request.POST.get('sdi')
    rewind_operation(request.user, sid)
    render_json(None)


def friends(request):
    data = [user.to_dict() for user in friends_operation(request.user)]
    render_json({'friends': data})
