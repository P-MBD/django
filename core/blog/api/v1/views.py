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
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

class PostModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['category', 'author', 'status']
    search_fields = ['title', 'content']

class CategoryModelViewSet(viewsets.ModelViewSet):
    permission_classes= [IsAuthenticated]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()




