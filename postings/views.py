import json

from django.views import View
from django.http  import JsonResponse

from postings.models import Post
from core.utils      import login_decorator

class PostingView(View):
    @login_decorator
    def post(self, request):
        try:
            data    = json.loads(request.body)
            title   = data['title']
            content = data['content']
            user    = request.user   
            
            Post.objects.create(
                title     = title,
                content   = content,
                image_url = data['image_url'],
                user_id   = user.id
            )
            return JsonResponse({'message':'Post Created!'}, status=201)
            
        except KeyError:
            return JsonResponse({'message':'KEY_ERROR'}, status=400)