import random, os
import requests
from django.conf import settings
from django.core.cache import cache
from swiper import config
from worker import call_by_worker
from lib.qiniucloud import upload_to_qiniu


def get_verify_code(length=6):
    """产生验证码"""
    return random.randrange(10 ** (length - 1), 10 ** length)


@call_by_worker
def send_verify_code(phone):
    """发送验证码 异步"""
    verify_code = str(get_verify_code())
    sms_config = config.values.copy()  # 浅拷贝（理解浅拷贝和深拷贝的区别），每次发送短信拼接自己的内容，不改变全局config
    sms_config['content'] = sms_config['content'] % verify_code
    sms_config['mobile'] = phone
    response = requests.post(url=config.url, data=sms_config)
    cache_key = "verify_code-%s" % phone
    cache.set(cache_key, verify_code, 120)  # 使用django自带的缓存保存验证码120s,ipython 函数？ 函数？？ 功能
    return response


def check_vcode(phonenum, vcode):
    cache_key = "verify_code-%s" % phonenum
    saved_vcode = cache.get(cache_key)
    return saved_vcode == vcode


def save_upload_file(upload_file, request):
    # 获取文件保存到本地
    file_type = os.path.splitext(upload_file.name)[-1]
    filename = 'avatar-%s%s' % (request.session['uid'], file_type)
    file_path = os.path.join(settings.BASE_DIR, settings.MEDIA_ROOT, filename)
    with open(file_path, 'wb') as f:
        for chunk in upload_file.chunks():
            f.write(chunk)
    # 上传文件到七牛云
    upload_to_qiniu(file_path, filename)
    # 将url写入数据库
    url = 'http://' + config.QN_BASE_URL + '/' + filename
    request.user.avatar = url
    request.user.save()
