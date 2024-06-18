from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializers import PostSerializer
from ...models import Post
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly,IsAdminUser
from rest_framework.views import APIView

"""@api_view(["GET","POST"])
@permission_classes([IsAdminUser])
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
            return Response(serializer.errors)"""

class PostList(APIView):
    """getting a list of posts and creating new posts"""
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    def get(self, request):
        """retriving a list of post """
        posts =Post.objects.filter(status=True)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    def post(self, request):
        """creating a post with providing data"""
        serializer = PostSerializer(data= request.data)
        if serializer.is_valid():
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

"""@api_view(["GET","PUT","DELETE"])
def postDetail(request,id):
    post = get_object_or_404(Post,pk=id)
    if request.method == "GET":
         serializer = PostSerializer(post)
         return Response(serializer.data)
    elif request.method =="PUT":
        serializer = PostSerializer(post, data= request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method =="DELETE":
        post.delete()
        return Response({"detail":"item removed successfully"},status=status.HTTP_204_NO_CONTENT)"""

class PostDetail(APIView):
    """getting detail of the post and edit plus removing it"""
    permission_classes =[IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    def get(self, request,id):
        """getting detail of the post and  edit plus removing it"""
        post=get_object_or_404(Post, pk=id)
        serializer = self.serializer_class(post)
        return Response(serializer.data)
    def put(self, request, id):
        """editing the post data"""
        post = get_object_or_404(Post, pk=id)
        serializer = self.serializer_class(post)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    def delete(self, request, id):
        post = get_object_or_404(Post, pk=id)
        post.delete()
        return Response({"detail":"item removed successfully"},status=status.HTTP_204_NO_CONTENT)




