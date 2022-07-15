import re

from django.core.exceptions import ValidationError

REGEX_EMAIL    = '^[a-zA-Z0-9]+@[a-zA-Z]+\.[a-zA-Z]+$'
REGEX_PASSWORD = '^(?=.*[A-Za-z])(?=.*\d)(?=.*[$@$!%*#?&])[A-Za-z\d$@$!%*#?&]{8,}$'
    
def validate_email(email):
    if not re.match(REGEX_EMAIL, email):
        # 여기가 왜 return이 아니고 raise인가?
        raise ValidationError('INVALID_EMAIL')
    
def validate_password(password):
    if not re.match(REGEX_PASSWORD, password):
        raise ValidationError('INVALID_PASSWORD')


# raise 대신 return 하게 되면 JsonResponse 객체를 반환할 뿐 코드는 계속해서 실행됨 #####
