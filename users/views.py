import json
import re

from django.http  import JsonResponse
from django.views import View

from users.models import User

class SignUpView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            
            name     = data['name']
            email    = data['email']
            password = data['password']
            phone    = data['phone']
            
            REGEX_EMAIL    = '^[a-zA-Z0-9]+@[a-zA-Z]+\.[a-zA-Z]+$'
            REGEX_PASSWORD = '^(?=.*[A-Za-z])(?=.*\d)(?=.*[$@$!%*#?&])[A-Za-z\d$@$!%*#?&]{8,}$'
            
            if not re.match(REGEX_EMAIL, email):
                return JsonResponse({'message':'Email is invalid.'}, status=400)
            
            if not re.match(REGEX_PASSWORD, password):
                return JsonResponse({'message':'Password is invalid.'}, status=400)
    
            User.objects.create(
                name     = name,
                email    = email,
                password = password,
                phone    = phone
            )
            
            return JsonResponse({'message':'SUCCESS'}, status=201)
    
        except KeyError:
            return JsonResponse({'message':'KEY_ERROR'}, status=400)
