from . import views
from django.urls import path


urlpatterns = [
    path("categories", views.CategoryList.as_view(), name="categories"),
    path("new", views.NewCategory.as_view(), name='new_category'),
]