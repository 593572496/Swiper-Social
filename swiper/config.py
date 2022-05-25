"""其他配置"""
"""三方短信验证平台"""
# 接口地址
url = 'http://106.ihuyi.com/webservice/sms.php?method=Submit'

# 定义请求的数据
values = {
    'account': 'C56662170',
    'password': '972f3001a6bddecb9e1c2dadc1d11815',
    'mobile': None,
    'content': '您的验证码是：%s。请不要把验证码泄露给其他人。',
    'format': 'json',
}
# 七牛云接入
QN_ACCESS_KEY = 'Zr1KAAylJs4gogpaFxfkBKMTIN869gh8I6gldZvk'
QN_SECRET_KEY = '-4BeBGcNX10X3Ryp5bQzqG4M2HksmdSnCtMpfFbT'
QN_BUCKET_KEY = 'swiper-wanli'
QN_BASE_URL = 'rcdjtdm7t.hn-bkt.clouddn.com'

