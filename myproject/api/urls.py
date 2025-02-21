from .views import test, PostListCreateView, PostDetailRetrieveUpdateDestroy
from django.urls import path

urlpatterns = [
    path('test/',test,name='test'),

    path('post/',PostListCreateView.as_view(),name='post-list-create'),
    path('post/<int:pk>/',PostDetailRetrieveUpdateDestroy.as_view(),name='post-detail-retrieve-update-destroy'),
]