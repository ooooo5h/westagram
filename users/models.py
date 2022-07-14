from django.db import models

# 모델의 이름은 단수
class User(models.Model):
    name     = models.CharField(max_length=50)
    email    = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=300)
    phone    = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # 데이터베이스 내에서 테이블을 식별할 때 사용하는 이름
    class Meta:
        db_table = 'users'
