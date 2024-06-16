from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PostSerializer
from ...models import Post
from django.shortcuts import get_object_or_404
data={
    "id":1,
    "title":"hello"
}

@api_view()
def postList(request):
    posts = get_object_or_404(Post, pk=id)
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)

@api_view()
def postDetail(request,id):
    post = get_object_or_404(Post,pk=id)
    print(post.__dict__)
    serializer = PostSerializer(post)
    return Response(serializer.data)

