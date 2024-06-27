from rest_framework.response import Response
from .serializers import PostSerializer,CategorySerializer
from ...models import Post, Category
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly,IsAdminUser
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView,ListCreateAPIView, RetrieveUpdateDestroyAPIView,RetrieveAPIView
from rest_framework import mixins, viewsets
from rest_framework.decorators import api_view, permission_classes, action
from .permissions import IsOwnerOrReadOnly
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

'''class PostList(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)
 '''
class PostModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)
    @action(methods = ["get"], detail=False)
    def get_ok(self, request):
        return Response({'detail','ok'})

class CategoryModelViewSet(viewsets.ModelViewSet):
    permission_classes= [IsAuthenticated]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
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

'''class PostDetail(APIView):
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
        return Response({"detail":"item removed successfully"},status=status.HTTP_204_NO_CONTENT)'''


class PostDetail(RetrieveUpdateDestroyAPIView):
    permission_classes =[IsAuthenticatedOrReadOnly] 
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)

