import bcrypt
import json
import jwt

from django.conf import settings
from django.http  import JsonResponse
from django.views import View

from users.models import User
from users.utils  import validate_email, validate_password

class SignUpView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            
            name     = data['name']
            email    = data['email']
            password = data['password']
            phone    = data['phone']
            
            validate_email(email)
            validate_password(password)    
            
            if User.objects.filter(email=email).exists():
                return JsonResponse({'message':'Email already exist'}, status=409)        
    
            User.objects.create(
                name     = name,
                email    = email,
                password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8'),
                phone    = phone
            )
            
            return JsonResponse({'message':'SUCCESS'}, status=201)
    
        except KeyError:
            return JsonResponse({'message':'KEY_ERROR'}, status=400)

class SignInView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            
            email    = data['email']
            password = data['password']
            
            email_exist_user = User.objects.get(email=email)
            
            if not email_exist_user :
                return JsonResponse({'message':'Email is Invalid'}, status=401)
            
            if not bcrypt.checkpw(password.encode('utf-8'), email_exist_user.password.encode('utf-8')):
                return JsonResponse({'message':'Password is Invalid'}, status=401)
            
            token = jwt.encode({'user_id':email_exist_user.id}, settings.SECRET_KEY, settings.ALGORITHM)
            
            return JsonResponse({'message':'SUCCESS', 'token':token}, status=200)
            
        except KeyError:
            return JsonResponse({'message':'KEY_ERROR'}, status=400)