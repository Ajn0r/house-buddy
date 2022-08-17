from . import views
from django.urls import path


urlpatterns = [
    path('blog', views.BlogList.as_view(), name='blog'),
    path('<slug:slug>/', views.BlogDetail.as_view(), name='blogpost'),
    path('like/<slug:slug>', views.LikePost.as_view(), name='post_like')
]