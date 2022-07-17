import jwt

from django.conf import settings
from django.http import JsonResponse

from users.models import User

def login_decorator(func):
    def wrapper(self, request, *args, **kwargs):
        try :
            # 토큰은 http header에 있다
            token        = request.headers.get('Authorization', None)
            # 토큰을 발급했을 때 encode했음. decode해서 user_id를 가져온다
            payload      = jwt.decode(token, settings.SECRET_KEY, settings.ALGORITHM)
            user         = User.objects.get(id=payload['user_id'])
            # 데코레이터를 받아 사용할 함수에 user정보를 request에 담아둠
            request.user = user
            
            return func(self, request, *args, **kwargs)
            
        except jwt.exceptions.DecodeError:
            return JsonResponse({'message':'서버에서 발급한 토큰 아님'}, status=400)
        
    return wrapper