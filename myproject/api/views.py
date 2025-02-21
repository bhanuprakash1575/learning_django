from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics

from blog.models import Post
from .serializer import PostSerializer



def test(request):
    return HttpResponse('Hello, World. this api test response!')

class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetailRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer