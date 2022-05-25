from django.utils.deprecation import MiddlewareMixin
from user.models import User
from lib.http import render_json
from common.error import LOGIN_ERROR


class AuthMiddleware(MiddlewareMixin):
    """用户登录中间件"""
    WHITE_LIST = [
        '/user/verify_code/',
        '/user/login/'
    ]

    def process_request(self, request):
        # 排除白名单中的url
        for url in self.WHITE_LIST:
            if request.path.startswith(url):
                return
        uid = request.session.get('uid')
        if uid:
            try:
                request.user = User.objects.get(id=uid)  # 将use绑定到request.user
                return
            except User.DoesNotExist:
                request.session.flush()
        return render_json(None, code=LOGIN_ERROR)
