import json


from django.http  import JsonResponse
from django.views import View

from users.models import User
from users.utils import validate_email, validate_password

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
    
            User.objects.create(
                name     = name,
                email    = email,
                password = password,
                phone    = phone
            )
            
            return JsonResponse({'message':'SUCCESS'}, status=201)
    
        except KeyError:
            return JsonResponse({'message':'KEY_ERROR'}, status=400)
