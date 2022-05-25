from lib.http import render_json
from user.logic import send_verify_code, check_vcode, save_upload_file
from user.models import User
from common import error
from user.forms import ProfileForms


def get_verify_code(request):
    """手机注册"""
    phonenum = request.POST.get('phonenum')
    print(phonenum)
    send_verify_code(phonenum)
    return render_json(None)


def login(request):
    """短信验证登录"""
    phonenum = request.POST.get('phonenum')
    vcode = request.POST.get('vcode')
    if check_vcode(phonenum, vcode):
        # 获取用户
        user, created = User.objects.get_or_create(phone=phonenum)
        request.session['uid'] = user.id
        return render_json(user.to_dict())

    else:
        return render_json(None, error.VCODE_ERROR)


def get_profile(request):
    """获取个人资料"""
    user = request.user
    print(request.path)
    return render_json(user.profile.to_dict())


def modify_profile(request):
    """修改个人资料"""
    form = ProfileForms(request.POST)
    if form.is_valid():
        user = request.user
        user.profile.__dict__.update(form.cleaned_data)  # 利用字典的update方法进行更新
        user.profile.save()
        return render_json(None)
    else:
        return render_json(form.errors, error.PROFILE_ERROR)


def upload_avatar(request):
    """头像上传"""
    upload_file = request.FILES.get('avatar')
    if upload_file:
        save_upload_file(upload_file, request)
        return render_json(None)
    else:
        return render_json(None, error.FILE_NOT_FOUND)
