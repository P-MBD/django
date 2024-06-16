from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PostSerializer
from ...models import Post
from django.shortcuts import get_object_or_404

@api_view(["GET","POST"])
def postList(request):
    if request.method == "GET":
        posts =Post.objects.filter(status=True)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = PostSerializer(data= request.data)
        if serializer.is_valid():
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

@api_view()
def postDetail(request,id):
    post = get_object_or_404(Post,pk=id)
    print(post.__dict__)
    serializer = PostSerializer(post)
    return Response(serializer.data)

