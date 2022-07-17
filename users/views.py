import bcrypt
import json

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
            
            if not User.objects.filter(email=email, password=password):
                return JsonResponse({'message':'Email or Password Invalid'}, status=401)
            
            return JsonResponse({'message':'SUCCESS'}, status=200)
            
        except KeyError:
            return JsonResponse({'message':'KEY_ERROR'}, status=400)