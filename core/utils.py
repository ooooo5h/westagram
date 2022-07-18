import jwt

from django.conf import settings
from django.http import JsonResponse

from users.models import User

def login_decorator(func):
    def wrapper(self, request, *args, **kwargs):
        try :
            if 'Authorization' not in request.headers:
                # Authorization이 없이 전달된 경우
                return JsonResponse({'message':'KEY_ERROR'}, status=400)
            
            token        = request.headers.get('Authorization')
            payload      = jwt.decode(token, settings.SECRET_KEY, settings.ALGORITHM)
            user         = User.objects.get(id=payload['user_id'])  # 이 키를 이용해서?
            request.user = user            
            
        except jwt.exceptions.DecodeError:
            # 우리가 보낸 토큰이 아닐 때 (서명)
            return JsonResponse({'message':'INVALID_TOKEN'}, status=400)
        
        except User.DoesNotExist:           
            # db에 유효하지않은 유저일 때                                 
            return JsonResponse({'message' : 'INVALID_USER'}, status=400)
                
        return func(self, request, *args, **kwargs)
    return wrapper