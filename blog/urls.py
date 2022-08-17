from . import views
from django.urls import path


urlpatterns = [
    path('blog', views.BlogList.as_view(), name='blog'),
    path('<slug:slug>', views.BlogDetail.as_view(), name='blogpost'),
    path('comment/<slug:slug>', views.PostComment.as_view(), name='comment'),
]